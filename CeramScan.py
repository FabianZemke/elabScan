# Standard libraries
import sys
import os

# For logging errors.
#import logging
#import time
import datetime

# For reading the excel table with the users
import pandas as pd
import numpy as np

# Import the other python files, resource files,..
from Ui_MainWindow import *
from Gui_GetSet import *

from PySide6.QtWidgets import QFileDialog, QComboBox, QRadioButton, QButtonGroup, QDateEdit
from PySide6.QtCore import QResource, QDateTime, Qt

# For the actual QR Coder
import qrcode

# For the printer connection
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from brother_ql.raster import BrotherQLRaster

# For decoding of the QR code1
import cv2

# For writing with the API
import elabapi_python
from elabapi_python.rest import ApiException
import urllib3
import json

# For image manipulation of the QR codes
from PIL import Image, ImageDraw, ImageFont
import io
import cairosvg
import tempfile

# For the REST API
import requests

# Global folders
## The Python folder with the main python file
global pythonfolder
pythonfolder = os.path.dirname(os.path.abspath(__file__))
## The Output folder
global outputfolder
outputfolder = os.path.join(pythonfolder, "Output")

global configdict
configdict = dict()

# Config File
try:
    with open(os.path.join(pythonfolder, "config.txt")) as f:
        lines = f.readlines()
        
        for line in lines:
            if len(line) != 0 and line != "\n":
                # Split each line into key and value
                key, value = map(str.strip, line.split('='))
                configdict[key] = value

        print(configdict)

except Exception as a:
    errorpath = os.path.join(outputfolder, "errorlog.txt")
    f = open(errorpath, "a")
    f.write(str(a) + "\n")
    f.close()

QResource.registerResource("Resourcefile_rc.py")

# Config File
try:
    with open(os.path.join(pythonfolder, "ElabTemplates", "Chemical.json")) as f:
        global chemicaltemplate
        chemicaltemplate = json.load(f)
        print(chemicaltemplate)

except Exception as a:
    errorpath = os.path.join(outputfolder, "errorlog.txt")
    with open(errorpath, "a") as f:
        f.write(str(a) + "\n")

global ceramscanversion
ceramscanversion = "CeramScan v1.618"

####################################################################################################################################
# Gui MainWindow
####################################################################################################################################


class Gui(QMainWindow, Ui_MainWindow, Gui_GetSet): #, MainWindow
    def __init__(self):
        super(Gui, self).__init__()
        self.setupUi(self)

        self.is_initial = False # BOOL
        self.initial = "" # STR
        self.shortday = "" # STR
        self.shortmonth = "" # STR
        self.shortyear = "" # STR

        self.samplenumberlist = [1]
        self.subsamplenumberlist = []

        self.is_batch = False # BOOL
        self.is_singlesubsample = False # BOOL
        self.is_batchsubsample = False # BOOL

        self.ghsdict = { # DICT
            "Explosive":False, 
            "Flammable":False, 
            "Oxidizing":False, 
            "Corrosive":False, 
            "Toxic":False, 
            "Harmful":False, 
            "HealthHazard":False, 
            "EnvironmentalHazard":False
            }
        self.disposal = "NoIdea"        
        self.df = None # This is the Pandas dataframe with all the data.

        self.savefolder = outputfolder

        self.hidden_tabs = {}

        # The dictionary for the chemical addition
        self.DictionarySelf = {}

        self.filledbypubchem = False

        self.chemjson = ""


        ####################################################################################################################################
        # Load the userid excel table. 
        userid = pd.read_excel(str(configdict["LinkID"]),"userid")
        userid = userid.apply(lambda x: x.astype(str).str.upper())

        ####################################################################################################################################
        # Start the program at home and set all tabs to the first position. And some stuff not visible.
        self.Main_tab.setCurrentIndex(0)
        self.Home_tab.setCurrentIndex(0)
        self.AddChemical_tab.setCurrentIndex(0)
        self.SampleID_tab.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        self.Subsample1_spinBox.setVisible(False)
        self.Subsample2_spinBox.setVisible(False)
        self.Subsample3_spinBox.setVisible(False) 
        self.label_11.setVisible(False)

        # Set some tabs to be invisble
        self.hide_tab_by_name(self.Main_tab, "Chemical_Main_tab")
        self.hide_tab_by_name(self.AddChemical_tab, "SelectChemical_tab")

        # Set the current date
        self.Current_dateEdit.setDateTime(QDateTime(QDate.currentDate(), QTime.currentTime()))
        date = self.Current_dateEdit.date().toPython()
        year = int(date.strftime("%Y")) + 10
        month = int(date.strftime("%m"))
        day = int(date.strftime("%d"))
        self.Current_dateEdit.setDisplayFormat("dd/MM/yyyy")
        self.Expiration_dateEdit.setDateTime(QDateTime(QDate(year,month,day), QTime.currentTime()))
        self.Expiration_dateEdit.setMinimumDateTime(QDateTime(QDate.currentDate(), QTime.currentTime()))
        self.Expiration_dateEdit.setDisplayFormat("dd/MM/yyyy")

        # Set the column width
        self.AddInformation_tableWidget.setColumnWidth(3, 80)
        self.AddInformation_tableWidget.setColumnWidth(4, 80)
        self.AddInformation_tableWidget.setColumnWidth(5, 80)

        ####################################################################################################################################
        # Button clicks and actions.
        #### Home ####
        self.HomeCreate_button.clicked.connect(lambda: self.tabchange(self.Main_tab, 1))
        self.HomeSearch_button.clicked.connect(lambda: self.tabchange(self.Main_tab, 2))
        self.HomeScan_button.clicked.connect(lambda: self.tabchange(self.Main_tab, 3))

        #### Advanced ####
        self.HomeLog_button.clicked.connect(lambda: self.tabchange(self.Main_tab, 4))
        self.HomeAbout_button.clicked.connect(lambda: self.tabchange(self.Main_tab, 5))
        self.HomeAddChemical_button.clicked.connect(lambda: (self.unhide_tab_by_name(self.Main_tab, "Chemical_Main_tab"), self.fill_scrollarea_from_template(chemicaltemplate, [self.Addchemical_current_scrollarea, self.Addchemical_supplier_scrollarea, self.Addchemical_datasheet_scrollarea, self.Addchemical_hpstatements_scrollarea]), self.tabchange(self.Main_tab, 6)))

        #### CreateSampleID ####
        self.SampleID_tab.currentChanged.connect(self.create_sampletable) # Tabchange connect.

        self.SampleidBack1_button.clicked.connect(lambda: self.tabchange(self.Main_tab, 0))
        self.SampleidForward1_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 1))
        self.Decrypt_button.clicked.connect(lambda: self.decrypt_abbr(userid))

        self.SampleidBack2_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 0))
        self.SampleidForward2_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 2))
        self.FirstName_lineEdit.textChanged.connect(lambda: self.namedate_update(userid)) 
        self.LastName_lineEdit.textChanged.connect(lambda: self.namedate_update(userid))
        self.Supervisor_lineEdit.textChanged.connect(lambda: self.upper_lineedit(self.Supervisor_lineEdit))
        self.Current_dateEdit.dateChanged.connect(lambda: self.namedate_update(userid))

        self.SampleidBack3_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 1))
        self.SampleidForward3_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 3))
        self.SubSample1_checkBox.stateChanged.connect(self.subsamplesingle_change)
        self.SubSample2_checkBox.stateChanged.connect(self.subsamplebatch_change)
        self.Batch_radioButton.toggled.connect(self.switch_singlebatch) 
        self.Samplenumber1_spinBox.valueChanged.connect(self.encrypt_samplenumber)
        self.Subsample1_spinBox.valueChanged.connect(self.encrypt_samplenumber)
        self.Samplenumber2_spinBox.valueChanged.connect(self.encrypt_samplenumber)
        self.Samplenumber3_spinBox.valueChanged.connect(self.encrypt_samplenumber)
        self.Subsample2_spinBox.valueChanged.connect(self.encrypt_samplenumber)
        self.Subsample3_spinBox.valueChanged.connect(self.encrypt_samplenumber)

        self.SampleidBack4_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 2))
        self.SampleidForward4_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 4))
        self.Explos_checkBox.stateChanged.connect(lambda: self.ghs_change("Explosive", self.Explos_checkBox))
        self.Flamme_checkBox.stateChanged.connect(lambda: self.ghs_change("Flammable", self.Flamme_checkBox))
        self.Rondflam_checkBox.stateChanged.connect(lambda: self.ghs_change("Oxidizing", self.Rondflam_checkBox))
        self.Acid_checkBox.stateChanged.connect(lambda: self.ghs_change("Corrosive", self.Acid_checkBox))
        self.Skull_checkBox.stateChanged.connect(lambda: self.ghs_change("Toxic", self.Skull_checkBox))
        self.Exclam_checkBox.stateChanged.connect(lambda: self.ghs_change("Harmful", self.Exclam_checkBox))
        self.Silhouette_checkBox.stateChanged.connect(lambda: self.ghs_change("HealthHazard", self.Silhouette_checkBox))
        self.Pollu_checkBox.stateChanged.connect(lambda: self.ghs_change("EnvironmentalHazard", self.Pollu_checkBox))

        self.SampleidBack5_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 3))
        self.SampleidForward5_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 5))
        self.NoIdea_radioButton.toggled.connect(lambda: self.disposal_change("NoIdea"))
        self.NonHarzardous_radioButton.toggled.connect(lambda: self.disposal_change("NonHazardous"))
        self.ContaminatedSolids_radioButton.toggled.connect(lambda: self.disposal_change("ContaminatedSolids"))
        self.HalogenatedSolvents_radioButton.toggled.connect(lambda: self.disposal_change("HalogenatedSolvents"))
        self.HalogenFreeSolvents_radioButton.toggled.connect(lambda: self.disposal_change("HalogenFree"))
        self.SpecialPrecautions_radioButton.toggled.connect(lambda: self.disposal_change("SpecialPrecautions"))

        self.SampleidBack6_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 4))
        self.SampleidForward6_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 6))
        #Recursion Error
        #self.AddInformation_tableWidget.itemChanged.connect(self.create_sampletable)

        self.SampleidBack7_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 5))
        self.SampleidForward7_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 7))
        self.Foldersave_button.clicked.connect(lambda: self.save_folder()) 
        self.Save_button.clicked.connect(lambda: self.save_qrcodes()) 
        self.ElabFTW_button.clicked.connect(lambda: self.sampleid_to_elabftw())
        self.Print_button.clicked.connect(lambda: self.print_qrcodes())

        self.SampleidBack8_button.clicked.connect(lambda: self.tabchange(self.SampleID_tab, 6))
        self.Reset_button.clicked.connect(lambda: self.reset_ceram())

        #### SearchSampleID ####

        self.SearchID_lineEdit.setEnabled(False)
        self.SearchID_pushButton.setEnabled(False)
        self.SearchID_textBrowser.setEnabled(False)

        #### ScanQR-Code ####

        self.ScanQR_button.setEnabled(False)
        self.ShowQR_button.setEnabled(False)
        self.ScanToCreate_button.setEnabled(False)
        self.ScanResult_textBrowser.setEnabled(False) 

        #### ShowTheLog ####


        #### About ####


        #### AddChemical ####

        self.AddChemical_fromID_button.clicked.connect(lambda: (self.create_chemicalfromid(), self.fill_chemdatabase_from_dict([self.Addchemical_datasheet_scrollarea, self.Addchemical_hpstatements_scrollarea]), self.tabchange(self.AddChemical_tab, 1)))

        self.ChemicalAdd_CreateNew_button.setEnabled(False)
        self.ChemicalAdd_CreatefromOld_button.setEnabled(False)

        self.AddChemicalToElab_button.clicked.connect(lambda: (self.chemicalinfo_to_json([self.Addchemical_current_scrollarea, self.Addchemical_supplier_scrollarea, self.Addchemical_datasheet_scrollarea, self.Addchemical_hpstatements_scrollarea]), self.chemid_to_elabftw()))

    ####################################################################################################################################
    # Other functions
    ####################################################################################################################################


    def get_allselfs(self):
        """
        Prints all the current values of instance variables (self attributes).

        Attributes:
        - self.is_initial (bool): Flag indicating if initials are available.
        - self.initial (str): User abbreviation generated from first and last names.
        - self.is_singlesubsample (bool): Flag indicating the presence of single subsamples.
        - self.is_batchsubsample (bool): Flag indicating the presence of batch subsamples.
        - self.is_batch (bool): Flag indicating if in batch sample mode.
        - self.ghsdict (dict): Dictionary containing GHS values.
        - self.disposal (str): Disposal information.
        - self.shortday (str): Abbreviation of the current day.
        - self.shortmonth (str): Abbreviation of the current month.
        - self.shortyear (str): Abbreviation of the current year.
        """
        print(
        "self.is_initial", self.is_initial,
        "self.initial", self.initial,
        "self.is_singlesubsample", self.is_singlesubsample,
        "self.is_batchsubsample", self.is_batchsubsample,
        "self.is_batch", self.is_batch,
        "self.ghsdict", self.ghsdict,
        "self.disposal", self.disposal,
        "self.shortday", self.shortday, 
        "self.shortmonth", self.shortmonth,
        "self.shortyear", self.shortyear
        )


    def decrypt_abbr(self, userid):
        """
        Translates an abbreviation of a user or sample ID to the lineedits.

        Parameters:
        - userid (pd.DataFrame): DataFrame containing user or sample ID information.

        Raises:
        - Exception: If the input is too short to be interpreted.

        Returns:
        None
        """
        outputtext = ""

        try:
            decryptinput = self.get_lineedit(self.Decrypt_lineEdit)
            if len(decryptinput) <= 1:
                self.create_log("Input is too short to be interpreted.")
                outputtext += "Input is too short to be interpreted; "
                raise Exception("Input is too short to be interpreted.")
            
            # Make sure that the rest of the date does not change if only a Year, i.e. a 3 character string, is given.
            year, month, day = self.get_date(self.Current_dateEdit)

            try:
                decrypt_id = userid[userid.UserID == decryptinput[0:2]].index.values
                self.set_lineedit(self.FirstName_lineEdit, userid.loc[decrypt_id,"First"].item().upper())
                self.set_lineedit(self.LastName_lineEdit, userid.loc[decrypt_id,"Surname"].item().upper())
                outputtext += "User ID was decrypted; "
            except:
                outputtext += "User ID is unknown; "

            if len(decryptinput) > 2:
                year_id = decryptinput[2]
                try:
                    year = self.decrypt_year(year_id, startingyear=int(configdict["StartingYear"]))
                    outputtext += "Year translated; "
                except TypeError:
                    # Log
                    outputtext += "Sample ID, wrong format for Year?; "
                    self.create_log("Sample ID, wrong format for Year?")
                    try:
                        year = int(configdict["StartingYear"])
                    except:
                        year = 2011

            if len(decryptinput) > 3:
                month_id = decryptinput[3]
                try:
                    month = self.decrypt_month(month_id)
                    outputtext += "Month translated; "
                except TypeError:
                    # Log
                    self.create_log("Sample ID too short to translate the month? Month set to 01.")
                    outputtext += "Month cannot be decrypted, set to 01; "
                    month = 1

            if len(decryptinput) > 4:
                day_id = decryptinput[4]
                try:
                    day = self.decrypt_day(day_id)
                    outputtext += "Day translated; "
                except TypeError:
                    # Log
                    self.create_log("Sample ID too short to translate the day? Day set to 01.")
                    outputtext += "Day cannot be decrypted, set to 01; "
                    day = 1

            self.set_date(self.Current_dateEdit,QDate(year, month, day))

        except Exception as e:
            outputtext += "Error: " + str(e)+ "; "
            self.create_log("Decrypt button: " + str(e))

        finally:
            self.set_label(self.DecryptResponse_label, outputtext)


    def encrypt_abbr(self, userid):
        """
        Translate the name to a user abbreviation.

        This method takes the first name and last name entered by the user, looks
        up the corresponding user ID in the provided 'userid' DataFrame, and returns
        the user abbreviation. If the user is found in the DataFrame, it returns
        the uppercase user ID. Otherwise, it generates an abbreviation using the
        first letters of the first and last names.

        Args:
        userid (pd.DataFrame): DataFrame containing user information.

        Returns:
        str: User abbreviation.
        """
        encrypt_firstname = self.get_lineedit(self.FirstName_lineEdit)
        encrypt_secondname = self.get_lineedit(self.LastName_lineEdit)

        try:
            if encrypt_secondname in userid.Surname.values and encrypt_firstname in userid.First.values:
                decrypt_id = userid[(userid["First"]==encrypt_firstname) & (userid["Surname"]==encrypt_secondname)].index.values
                self.initial = userid.loc[decrypt_id,"UserID"].item().upper()
                self.is_initial = True
            else:
                self.initial = "-" + encrypt_firstname[0:1].upper() + encrypt_secondname[0:1].upper()
                self.is_initial = False
        except:
            self.initial = "-" + encrypt_firstname[0:1].upper() + encrypt_secondname[0:1].upper()
            self.is_initial = False

        return self.initial
                

    def encrypt_date(self):
        """
        Translate the date to its abbreviation.

        This method extracts the year, month, and day from the current date and
        translates each component to its corresponding abbreviation. It returns a
        tuple containing the abbreviated year, month, and day.

        Returns:
        Tuple[str, str, str]: A tuple containing the abbreviated year, month, and day.
        """
        year, month, day = self.get_date(self.Current_dateEdit)
        try:
            self.shortyear = self.encrypt_year(year, startingyear=int(configdict["StartingYear"]))
        except:
            self.shortyear = self.encrypt_year(year, startingyear=2011)
        self.shortmonth = self.encrypt_month(month)
        self.shortday = self.encrypt_day(day)
        
        return (self.shortyear, self.shortmonth, self.shortday)


    def namedate_update(self, userid):
        """
        Update the Initial and date by any change of any of the fields.

        Args:
        userid (str): The user ID for encryption.

        Returns:
        None.
        """
        initial = self.encrypt_abbr(userid)
        (shortyear, shortmonth, shortday) =  self.encrypt_date()

        self.NameDateOutput_label.setText(str(str(initial)+ str(shortyear)+ str(shortmonth)+str(shortday))) 


    def subsamplesingle_change(self):
        """
        Change the state of single subsamples.

        This method toggles the state of single subsamples based on the visibility
        of certain UI elements. It updates the 'self.is_singlesubsample' attribute
        and adjusts the visibility of related UI elements accordingly.

        Returns:
        None.
        """
        self.is_singlesubsample = self.checkbox_visibilitychange(self.SubSample1_checkBox, self.Subsample1_spinBox)
        self.encrypt_samplenumber()
        self.create_log("The subsamples for single samples was changed to: " + str(self.is_singlesubsample))


    def subsamplebatch_change(self):
        """
        Change the state of batch subsamples.

        This method toggles the state of batch subsamples based on the visibility
        of certain UI elements. It updates the 'self.is_batchsubsample' attribute
        and adjusts the visibility of related UI elements accordingly.

        Returns:
        None.
        """
        self.is_batchsubsample = self.checkbox_visibilitychange(self.SubSample2_checkBox, self.Subsample2_spinBox)
        self.checkbox_visibilitychange(self.SubSample2_checkBox, self.Subsample3_spinBox)
        self.checkbox_visibilitychange(self.SubSample2_checkBox, self.label_11)
        self.checkbox_visibilitychange(self.SubSample2_checkBox, self.Samplenumber3_spinBox, inverse=True)
        self.checkbox_visibilitychange(self.SubSample2_checkBox, self.label_10, inverse=True)
        self.encrypt_samplenumber()
        self.create_log("The subsamples for batch samples was changed to: " + str(self.is_batchsubsample))


    def switch_singlebatch(self):
        """
        Switch between single and batch sample modes.

        This method toggles between single and batch sample modes based on the
        selection of the corresponding radio button. It updates the 'self.is_batch'
        attribute and logs the mode change.

        Returns:
        None.
        """
        if self.Batch_radioButton.isChecked():
            self.is_batch = True
            self.create_log("Batch sample mode: " + str(self.is_batch))
        else:
            self.is_batch = False
            self.create_log("Batch sample mode: " + str(self.is_batch))
        self.encrypt_samplenumber()
        

    def ghs_change(self, ghsdictkey, checkboxobject):
        """
        Change a GHS value in the GHS dictionary.

        Args:
        ghsdictkey (str): The key corresponding to the GHS value.
        checkboxobject (QCheckBox): The checkbox object representing the GHS value.

        Returns:
        None.
        """
        state = self.getstate_checkbox(checkboxobject)
        self.ghsdict[ghsdictkey] = state


    def disposal_change(self, disposalstring):
        """
        Change the disposal string.

        Args:
        disposalstring (str): The new disposal string.

        Returns:
        None.
        """
        self.disposal = disposalstring

    
    def encrypt_samplenumber(self):
        """
        Get the samplenumber(s) with potentially its subsamplenumber(s).

        This method retrieves sample numbers and subsample numbers based on user input.
        It ensures that the entered values are within a valid range and handles batch
        and single sample scenarios accordingly. The resulting sample numbers and
        subsample numbers are stored in 'self.samplenumberlist' and 'self.subsamplenumberlist'.

        Returns:
        None.
        """
        # If the first value is changed to be higher than the second.
        if self.Samplenumber2_spinBox.value() > self.Samplenumber3_spinBox.value():
            self.Samplenumber3_spinBox.setValue(self.Samplenumber2_spinBox.value())
        # If the first value is changed to be higher than the second.
        elif self.Subsample2_spinBox.value() > self.Subsample3_spinBox.value():
            self.Subsample3_spinBox.setValue(self.Subsample2_spinBox.value())
        # Currently, the maximum amount of samples is chosen to be 20 at a time.
        elif self.Subsample3_spinBox.value() >= (self.Subsample2_spinBox.value()+19):
            self.Subsample3_spinBox.setValue(self.Subsample2_spinBox.value()+19)
        elif self.Samplenumber3_spinBox.value() >= (self.Samplenumber2_spinBox.value()+19):
            self.Samplenumber3_spinBox.setValue(self.Samplenumber2_spinBox.value()+19)

        self.samplenumberlist = []
        self.subsamplenumberlist = []

        # If the batch sample number is selected:
        if self.is_batch:
            try:
                if self.is_batchsubsample:
                    self.subsamplenumberlist.extend(list(range(self.Subsample2_spinBox.value(), self.Subsample3_spinBox.value()+1)))
                    self.samplenumberlist.extend([self.Samplenumber2_spinBox.value()]*len(self.subsamplenumberlist))

                else:
                    self.samplenumberlist.extend(list(range(self.Samplenumber2_spinBox.value(), self.Samplenumber3_spinBox.value()+1)))
            except:
                pass

        # If the single sample number is selected:
        else:
            try:
                self.samplenumberlist.append(self.Samplenumber1_spinBox.value())
        
                if self.is_singlesubsample:
                    self.subsamplenumberlist.append(self.Subsample1_spinBox.value())
            except:
                pass

        print("SampleNumber", self.samplenumberlist, "SubSample", self.subsamplenumberlist)


    def create_sampletable(self):
        """
        Create the sampleID table with buttons.

        This method populates the sampleID table in the GUI with sample information.
        It retrieves necessary data using 'get_allselfs()' and iterates over the sample
        numbers to create labels with short names and numbers. The information is then
        added to the 'AddInformation_tableWidget'.

        Returns:
        None.
        """
        
        self.get_allselfs()

        for i in range(len(self.samplenumberlist)):
            shortname = str(self.NameDateOutput_label.text())
            if len(self.subsamplenumberlist) != 0:
                number = str(self.samplenumberlist[i]) + "_" + str(self.subsamplenumberlist[i])
            else:
                number = str(self.samplenumberlist[i])
            #self.AddInformation_tableWidget.setCellWidget(i,0, QLabel(shortname+number)) #
            self.AddInformation_tableWidget.setItem(i,0, QTableWidgetItem(shortname+number))


    def get_pdsamples(self):
        """
        Generate a pandas DataFrame for all samples.

        This method collects information from the GUI elements and creates a DataFrame
        containing sample-related information. It extracts data such as sample IDs,
        custom sample names, additional comments, and boolean values for ElabFTW, Save PNG,
        and Print. The DataFrame is then populated with this information.

        Returns:
        None. The method updates the 'df' attribute with the generated DataFrame.
        """
        self.df = pd.DataFrame()
        sampleidlist = []
        customsamplelist = []
        Addcommentslist = []
        elablist = []
        savelist = []
        printlist = []

        firstname = self.get_lineedit(self.FirstName_lineEdit, upper = True)
        secondname = self.get_lineedit(self.LastName_lineEdit, upper = True)
        supervisor = self.get_lineedit(self.Supervisor_lineEdit, upper = True)
        year, month, day = self.get_date(self.Current_dateEdit)
        expyear, expmonth, expday = self.get_date(self.Expiration_dateEdit)
        
        for i in range(len(self.samplenumberlist)):
            # Sample ID
            if self.AddInformation_tableWidget.item(i,0):
                sampleidlist.append(self.AddInformation_tableWidget.item(i,0).text())
            else:
                sampleidlist.append("")

            # Custom Sample Name
            if self.AddInformation_tableWidget.item(i,1):
                customsamplelist.append(self.AddInformation_tableWidget.item(i,1).text())
            else:
                customsamplelist.append("")

            # Additional Comments
            if self.AddInformation_tableWidget.item(i,2):
                Addcommentslist.append(self.AddInformation_tableWidget.item(i,2).text())
            else:
                Addcommentslist.append("")

            # ElabFTW bool
            if self.AddInformation_tableWidget.item(i,3).checkState() == Qt.Checked:
                elablist.append(True)
            else:
                elablist.append(False)

            # Save PNG bool
            if self.AddInformation_tableWidget.item(i,4).checkState() == Qt.Checked:
                savelist.append(True)
            else:
                savelist.append(False)

            # Print bool
            if self.AddInformation_tableWidget.item(i,5).checkState() == Qt.Checked:
                printlist.append(True)
            else:
                printlist.append(False)

        self.df["First name"] = [firstname] * len(self.samplenumberlist)
        self.df["Surname"] = [secondname] * len(self.samplenumberlist)
        self.df["SampleID"] = sampleidlist
        self.df["Supervisor"] = [supervisor] * len(self.samplenumberlist)
        self.df["Date"] = [str(year) + "-" + str(month) + "-" + str(day)] * len(self.samplenumberlist)
        self.df["Expiration Date"] = [str(expyear) + "-" + str(expmonth) + "-" + str(expday)] * len(self.samplenumberlist)
        self.df["Custom Sample Name"] = customsamplelist
        self.df["Additional Comments"] = Addcommentslist
        self.df["ElabList"] = elablist
        self.df["SaveList"] = savelist
        self.df["PrintList"] = printlist
        self.df["GHS"] = [self.ghsdict] * len(self.samplenumberlist)
        self.df["Disposal"] = [self.disposal] * len(self.samplenumberlist)
        print(self.df)


    def save_folder(self):
        """
        Select a folder for saving the QR code images.

        This method opens a dialog for selecting a folder and sets the 'savefolder' attribute
        to the chosen path. It also logs the changes and updates labels in the GUI accordingly.

        Raises:
        - If an error occurs during the folder selection, an error message is logged,
        and error labels are updated in the GUI.

        Note:
        - If the folder selection is canceled, the method does not change the 'savefolder' attribute.
        - If the selected folder is empty, the default output folder is used.

        Returns:
        None. The method updates the 'savefolder' attribute based on the user's choice and logs the changes.
        """
        try:
            folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
            self.savefolder = str(folder)
            # Log
            self.create_log("Changed folderpath: " + str(self.savefolder) + ".")
            self.set_label(self.ElabFTWOutput1_label, "Changed folderpath: ")
            self.set_label(self.ElabFTWOutput2_label, str(self.savefolder) + ".")
        except:
            # Log
            self.create_log("Did not change the folderpath.")
            self.set_label(self.ElabFTWOutput1_label, "Error: ")
            self.set_label(self.ElabFTWOutput2_label, "Did not change the folderpath.")
        if len(self.savefolder) < 1:
            self.savefolder = outputfolder
            # Log
            self.create_log("Default folderpath. "+ self.savefolder)
            self.set_label(self.ElabFTWOutput1_label, "Changed folderpath: ")
            self.set_label(self.ElabFTWOutput2_label, str(self.savefolder) + ".")


    def qr_create(self):
        """
        Generate QR code images with additional labels.

        This method performs the following steps:
        1. Retrieves sample data using the 'get_pdsamples' method.
        2. Iterates through the sample data and creates a QR code for each entry.
        3. Adds labels to the QR code, including Shortname, Username, and GHS symbols.
        4. Combines all components into a single image and appends it to the 'qrlist' attribute.

        Note:
        - The Shortname and Username labels are rotated 90 degrees for better layout.
        - GHS symbols are added based on the hazard information in the sample data.

        Returns:
        None. The method generates QR codes and updates the 'qrlist' attribute, and there is no explicit return value.
        """
        self.get_pdsamples()
        self.qrlist = []
        qr = ""

        for i in range(len(self.df["SampleID"])):
            for j in self.df.columns:
                # Exclude some columns.
                if j not in ["GHS", "Additional Comments", "Expiration Date", "Disposal", "Custom Sample Name", "ElabList", "SaveList", "PrintList"]:
                    qr += str(self.df[j].iloc[i]) + ";\n"
            
            qrmake = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=0
            )
            qrmake.add_data(str(qr))
            qrmake.make(fit=True)
            img = qrmake.make_image(fill_color="black", back_color="white")

            # Create icons and named QR code.
            username = str(self.df["First name"].iloc[i]) + " " + str(self.df["Surname"].iloc[i])

            try:
                font = ImageFont.truetype("FreeMono.ttf", 40)
            except:
                font = ImageFont.truetype("arial.ttf", 40)
            
            # Create the Shortname label
            Shortname_im = Image.new("RGB", (img.size[0],40), color="white")
            ShortnameText = ImageDraw.Draw(Shortname_im)
            ShortnameText.text((0, 0), str(self.df["SampleID"].iloc[i]), fill="black",  font=font)
            RotatedShortname = Shortname_im.rotate(90, expand=1)
            
            # Create the Username label
            Username_im = Image.new("RGB", (img.size[0],40), color="white")
            UsernameText = ImageDraw.Draw(Username_im)
            UsernameText.text((0, 0), username, fill="black",  font=font)
            RotatedUser = Username_im.rotate(90, expand=1)
            
            # Create the GHS symbols
            harmful_xoffset = 0
            new_xsize = int(np.round(np.divide(img.size[0],4))) # It is assumed that not more than 4 GHS symbols are clicked. Everything else should be unreasonable
            new_ysize = int(np.round(np.divide(img.size[1],4))) # It is assumed that not more than 4 GHS symbols are clicked. Everything else should be unreasonable

            hazarddict = {"Explosive":":/Images/hazard-explosive-icon.svg",
                          "Flammable":":/Images/hazard-flammable-icon.svg",
                          "Oxidizing":":/Images/hazard-oxidising-icon.svg",
                          "Corrosive":":/Images/hazard-corrosive-icon.svg",
                          "Toxic":":/Images/hazard-acute-toxicity-icon.svg",
                          "Harmful":":/Images/hazard-harmful-icon.svg",
                          "HealthHazard":":/Images/hazard-serious-health-icon.svg",
                          "EnvironmentalHazard":":/Images/hazard-environmental-icon.svg"
                          }

            Hazard_im = Image.new("RGB", (img.size[0],new_ysize), color="white")

            for j in hazarddict:
                if (self.df["GHS"].iloc[i][j]):                
                    # Access the image using the resource path
                    image_path = hazarddict[j]
                    # Get the image data from the resource
                    image_data = QResource(image_path).data()
                    # Convert SVG to PNG using cairosvg
                    png_data = cairosvg.svg2png(image_data, background_color="white")
                    # Convert the PNG data to a Pillow Image
                    pil_image = Image.open(io.BytesIO(png_data)).convert("RGBA")
                    resized_image = pil_image.resize((new_xsize, new_ysize))
                    Hazard_im.paste(resized_image,(harmful_xoffset,0))
                    harmful_xoffset += new_xsize
            
            # Calculate the total width
            totalwidth = img.size[0] + RotatedShortname.size[0] + RotatedUser.size[0] + 20
            totalheight = img.size[1] + new_ysize + 20
            
            # Finally combine everything to one image.
            combined_im = Image.new("RGB", (totalwidth,totalheight), color="white")
            x_offset = 10
            y_offset = 10
            combined_im.paste(RotatedShortname, (x_offset, y_offset))
            x_offset += RotatedShortname.size[0]
            y_offset += 0
            combined_im.paste(img, (x_offset, y_offset))
            x_offset += img.size[0]
            y_offset += 0
            combined_im.paste(RotatedUser, (x_offset, y_offset))
            x_offset = 10 + RotatedShortname.size[0]
            y_offset += img.size[1] + 10
            combined_im.paste(Hazard_im, (x_offset, y_offset))         
                        
            self.qrlist.append(combined_im)
            qr = ""


    def save_qrcodes(self):
        """
        Save QR codes based on the 'SaveList' in the DataFrame.

        This method performs the following steps:
        1. Calls the 'qr_create' method to generate QR codes.
        2. Iterates through the generated QR codes and saves them based on the 'SaveList' in the DataFrame.
        3. Logs the saved QR codes and updates labels in the GUI.

        Returns:
            None. The method saves QR codes to the specified folder and updates log information.
        """
        # Generate QR codes
        self.qr_create()

        # Iterate through QR codes and save based on 'SaveList'
        for i, qr in enumerate(self.qrlist):
            if self.df["SaveList"].iloc[i]:
                # Construct the save file path
                savefile = os.path.join(self.savefolder, str(self.df["SampleID"].iloc[i]) + ".png")
                # Save the QR code
                qr.save(savefile)
                # Log
                self.create_log("Saved QR code of "+ str(self.df["SampleID"].iloc[i]) + " at: " + self.savefolder)
                self.set_label(self.ElabFTWOutput1_label, "Success: ")
                self.set_label(self.ElabFTWOutput2_label, "Saved QR code of "+ str(self.df["SampleID"].iloc[i]) + ".")


    def elabftwbody_create(self):
        """
        Process sample data and create a list of dictionaries for eLabFTW.

        This method performs the following steps:
        1. Retrieves sample data using the 'get_pdsamples' method.
        2. Initializes an empty list 'elablist' to store dictionaries for eLabFTW.
        3. Iterates through the sample data and creates dictionaries for each sample.
        4. Each dictionary contains tags, title, body, and metadata fields for eLabFTW.
        5. Appends each dictionary to 'elablist'.

        Note:
            - The sample data is expected to be available in the global variable 'df'.
            - The list of sub-sample numbers is expected to be available in the global variable 'subsamplenumberlist'.
            - The list of sample numbers is expected to be available in the global variable 'samplenumberlist'.

        Returns:
            None. The method processes the sample data and populates the 'elablist' variable.
        """

        self.get_pdsamples()
        self.elablist = []
        elabdict = dict()

        for i in range(len(self.df["SampleID"])):
            
            # Add tags
            tags = []

            if self.df["SampleID"].iloc[i] != "":
                tags.append(str(self.df["SampleID"].iloc[i]))
            if self.df["First name"].iloc[i] != "":
                tags.append(str(self.df["First name"].iloc[i]))
            if self.df["Surname"].iloc[i] != "":
                tags.append(str(self.df["Surname"].iloc[i]))

            elabdict["tags"] = tags

            # Add the title
            elabdict["title"] = str(self.df["SampleID"].iloc[i])

            # Add the body
            current_datetime = datetime.datetime.now()

            if len(self.subsamplenumberlist) != 0:
                subnumber = int(self.subsamplenumberlist[i])
            else:
                subnumber = "None"

            # Using a lambda function and filter to get keys where the value is True
            ghs = "; ".join(filter(lambda key: self.df["GHS"].iloc[i][key], self.df["GHS"].iloc[i].keys()))

            body = f"""
            <b>Sample ID: </b> {str(self.df["SampleID"].iloc[i])} <br>
            <b>Log Time: </b> {str(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))} <br>
            <b>Firstname: </b> {str(self.df["First name"].iloc[i])} <br>
            <b>Lastname: </b> {str(self.df["Surname"].iloc[i])} <br>
            <b>Supervisor: </b> {str(self.df["Supervisor"].iloc[i])} <br>
            <b>Date: </b> {str(self.df["Date"].iloc[i])} <br>
            <b>Expiration: </b> {str(self.df["Expiration Date"].iloc[i])} <br>
            <b>Samplenumber: </b> {int(self.samplenumberlist[i])} <br>
            <b>Sub-Samplenumber: </b> {subnumber} <br>
            <b>GHS: </b> {str(ghs)} <br>
            <b>Disposal: </b> {str(self.df["Disposal"].iloc[i])} <br>
            <b>Custom Sample Name: </b> {str(self.df["Custom Sample Name"].iloc[i])} <br><br>
            {str(self.df["Additional Comments"].iloc[i])}
            """
            bodystrp = body.strip()
            elabdict["body"] = str(bodystrp)
            
            # Add the metadata/extra fields
            metadata = {"extra_fields":
                            {
                                "Sample_ID" : 
                                    {
                                    "type": "text",
                                    "value": str(self.df["SampleID"].iloc[i]),
                                    "description":f"SampleID created by {ceramscanversion}"
                                    },
                                "Date" : 
                                    {
                                    "type": "date",
                                    "value": str(self.df["Date"].iloc[i])
                                    },
                                "Expiration" : 
                                    {
                                    "type": "date",
                                    "value": str(self.df["Expiration Date"].iloc[i])
                                    },
                                "Custom_Sample_Name" : 
                                    {
                                    "type": "text",
                                    "value": str(self.df["Custom Sample Name"].iloc[i])
                                    },
                                "Institution" : 
                                    {
                                    "type": "text",
                                    "value": str(configdict["Institution"])
                                    }                            
                            }
                        }
            elabdict["metadata"] = metadata

            # Save this entry to a list of dictionaries
            self.elablist.append(elabdict)
            # Empty the temporary dictionary
            elabdict = dict()

        print(self.elablist)


    def sampleid_to_elabftw(self):
        """
        Upload sample data to eLabFTW.

        This method performs the following steps:
        1. Generates QR codes and saves them as PNG images.
        2. Creates a dictionary for eLabFTW data based on sample information.
        3. Configures the eLabFTW API client using the provided API key and base URL.
        4. Initializes the eLabFTW ItemsApi for working with eLabFTW items.
        5. Iterates through the sample data, creates new items in eLabFTW, and modifies their properties.

        Note:
            - The configuration information, such as API key, base URL, and category ID, is expected to be
            available in the global variable 'configdict'.
            - The sample data is expected to be available in the global variable 'elablist'.
            - QR codes are generated using the 'qr_create' method.
            - eLabFTW data is created using the 'elabftwbody_create' method.

        Returns:
            None. The method performs API requests to create and modify items, 
            and there is no explicit return value.

        Inputs:
            - self: The instance of the class containing this method.
        """

        # QR png-list
        self.qr_create()

        # elabdict create
        self.elabftwbody_create()

        # These lines configure the eLabFTW API client using the provided API key and base URL. It also sets additional configurations, such as disabling SSL verification and debugging.
        configuration = elabapi_python.Configuration()
        configuration.api_key['api_key'] = configdict["API_Key"]
        configuration.api_key_prefix['api_key'] = 'Authorization'
        configuration.host = configdict["ElabFTW_URL"]
        configuration.debug = False
        configuration.verify_ssl = False

        # This creates an instance of the eLabFTW API client (api_client) with the specified configuration. It also fixes an issue related to the Authorization header not being properly set by the generated library.
        api_client = elabapi_python.ApiClient(configuration)
        api_client.set_default_header(header_name='Authorization', header_value=configdict["API_Key"])

        # This line initializes the ItemsApi class using the configured API client. It provides an interface for working with eLabFTW items.
        itemsApi = elabapi_python.ItemsApi(api_client)
        # Create an instance for uploads.
        uploadsApi = elabapi_python.UploadsApi(api_client)

        # Disable SSL warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        for i, elab in enumerate(self.elablist):
            if self.df["ElabList"].iloc[i]:
                print(elab["metadata"])

                # This section demonstrates creating a new item with the specified category and tags. It then retrieves the newly created item's ID from the response and modifies its title, body, and rating.
                targetCategory = configdict["Category_ID"]
                response = itemsApi.post_item_with_http_info(body={'category_id': targetCategory, 'tags': elab["tags"]})
                locationHeaderInResponse = response[2].get('Location')
                itemId = int(locationHeaderInResponse.split('/').pop())
                itemsApi.patch_item(itemId, body={'title': elab["title"], 'body': elab["body"], "metadata" : json.dumps(elab["metadata"])}) #, 'rating': 5

                # Create a temporary file.
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png") 
                with open(temp_file.name, 'wb') as file:
                    image_bytes_io = io.BytesIO()
                    self.qrlist[i].save(image_bytes_io, format="PNG")
                    image_bytes = image_bytes_io.getvalue()
                    file.write(image_bytes)

                # upload the file produced before.
                uploadsApi.post_upload("items", itemId, file = temp_file.name, comment = f"Uploaded with {ceramscanversion} using elabapi.")
                temp_file.close()
                os.unlink(temp_file.name)

                print(f'The newly created item is here: {locationHeaderInResponse}')

                # Log
                self.create_log("Saved sample "+ str(self.df["SampleID"].iloc[i]) + " to elabFTW at: " + locationHeaderInResponse)
                self.set_label(self.ElabFTWOutput1_label, "Success: ")
                self.set_label(self.ElabFTWOutput2_label, "Saved sample "+ str(self.df["SampleID"].iloc[i]) + " to elabFTW.")


    def print_qrcodes(self):
        """
        Print QR codes using a Brother QL label printer.

        This method performs the following steps:
        1. Generates QR codes using the 'qr_create' method.
        2. Combines the generated QR codes based on the selected layout.
        3. Resizes the combined image to the specified target width.
        4. Prints the resized image on a Brother QL label printer.

        Note:
        - The layout options include "15 mm", "20 mm", "30 mm", and "60 mm".
        - The target width is set to 62 mm with a DPI of 300.
        - The 'combine_images' function arranges QR codes based on the selected layout.
        - The 'resize_image' function resizes an image while maintaining its aspect ratio.
        - The Brother QL label printer configuration (model, printer address) is specified in the method.

        Returns:
        None. The method performs image processing and printing actions, and there is no explicit return value.
        """
        # Generate QR codes
        self.qr_create()

        def combine_images(images, selected_layout):
            # Image sizes for each layout
            layout_sizes = {
                "15 mm": (4, 1),
                "20 mm": (3, 1),
                "30 mm": (2, 1),
                "60 mm": (1, 1),
            }

            # Check if the selected layout is valid
            if selected_layout not in layout_sizes:
                raise ValueError(f"Invalid layout: {selected_layout}")

            # Get the layout size
            layout_width, layout_height = layout_sizes[selected_layout]

            # Calculate the number of rows needed
            num_rows = -(-len(images) // layout_width)  # Equivalent to math.ceil(len(images) / layout_width)

            # Create a white background image for the layout
            background_color = (255, 255, 255)  # White
            layout_image = Image.new("RGB", (layout_width * images[0].width, layout_height * num_rows * images[0].height), background_color)

            # Paste images onto the layout
            for i in range(len(images)):
                col = i % layout_width
                row = i // layout_width
                x_offset = col * images[i].width
                y_offset = row * images[i].height
                layout_image.paste(images[i], (x_offset, y_offset))

            return layout_image
        
        def resize_image(original_image, target_width_mm, dpi):
            # Calculate the target width in pixels based on DPI
            target_width_pixels = int((target_width_mm / 25.4) * dpi)
            # Calculate the proportional height
            target_height_pixels = int((target_width_pixels / float(original_image.size[0])) * original_image.size[1])
            # Resize the image
            resized_image = original_image.resize((target_width_pixels, target_height_pixels), Image.ANTIALIAS)
            return resized_image

        # Assuming you have a list of PIL images called 'image_list'
        image_list = []
        for i, qr in enumerate(self.qrlist):
            if self.df["PrintList"].iloc[i]:#
                image_list.append(qr)

        # Select the layout
        selected_layout = str(self.PrintLayout_comboBox.currentText()).strip()

        # Combine images based on the selected layout
        combined_image = combine_images(image_list, selected_layout)

        target_width_mm = 62
        dpi = 300

        resized_image = resize_image(combined_image, target_width_mm, dpi)
        #resized_image.show()  # Display the resized image

        backend = 'network' 
        model = 'QL-1050' # your printer model.
        printer = 'tcp://130.149.94.96:9100'    # Get these values from the Windows usb driver filter.  Linux/Raspberry Pi uses '/dev/usb/lp0'.

        qlr = BrotherQLRaster(model)
        qlr.exception_on_warning = True

        instructions = convert(
                qlr=qlr, 
                images=[resized_image],    #  Takes a list of file names or PIL objects.
                label='62', 
                rotate='0',    # 'Auto', '0', '90', '270'
                threshold=70.0,    # Black and white threshold in percent.
                dither=False, 
                compress=False, 
                red=False,    # Only True if using Red/Black 62 mm label tape.
                dpi_600=False, 
                hq=True,    # False for low quality.
                cut=True
        )

        send(instructions=instructions, printer_identifier=printer, backend_identifier=backend, blocking=True)

        # Log
        self.create_log("Printed samples")
        self.set_label(self.ElabFTWOutput1_label, "Printed samples")
        self.set_label(self.ElabFTWOutput2_label, "")


    def reset_ceram(self):
        """
        Restart the Ceram application.

        This method restarts the Ceram application by replacing the current process with a new
        instance of the Python interpreter running the same script. It effectively terminates
        the current instance and starts a fresh one.

        Usage:
            - Call this method when you want to reset the Ceram application.

        Note:
            - Any unsaved state or context will be lost during the restart.

        Parameters:
            None

        Returns:
            None
        """
        python_executable = sys.executable  # Get the path to the Python interpreter
        script_path = sys.argv[0]  # Get the path to the current script
        # Replace the current process with a new instance of the Python interpreter with the current script
        os.execl(python_executable, python_executable, script_path)


    def create_log(self, logtext):
        """
        Log current time and provided text to the text browser.

        This method performs the following steps:
        1. Retrieves the current date and time using QDateTime.
        2. Formats the current date and time as a string in the format "%Y-%m-%d %H:%M".
        3. Combines the formatted time with the provided log text.
        4. Appends the combined log entry to the text browser.

        Parameters:
            logtext (str): The text to be logged along with the current time.

        Returns:
            None. The method updates the Log_textBrowser with the current time and log text.
        """
        # Get the current date and time as a string
        currenttime = QDateTime.currentDateTime().toPython().strftime("%Y-%m-%d %H:%M")
        # Combine the formatted time with the provided log text
        Timelog = f"{currenttime}: {logtext}"
        # Append the log entry to the text browser
        self.Log_textBrowser.append(Timelog)


    def fill_scrollarea_from_template(self, json, scroll_areas):
        """
        Fills the provided scroll areas with widgets based on the template provided in json_data.

        The function iterates over the 'extra_fields' in the json_data. Depending on the 'type' of each field,
        it creates a corresponding widget (QLineEdit, QComboBox, or a group of QCheckBoxes/QRadioButtons).
        These widgets are then added to the layout of the scroll area corresponding to the 'group_id' of the field.

        Parameters:
        json_data (dict): A dictionary containing the template for the fields.
        scroll_area1 (QScrollArea): The first scroll area to be filled.
        scroll_area2 (QScrollArea): The second scroll area to be filled.
        scroll_area3 (QScrollArea): The third scroll area to be filled.
        scroll_area4 (QScrollArea): The fourth scroll area to be filled.

        Returns:
        None
        """
        try:
            for scroll_area in scroll_areas:
                widget = QWidget()
                layout = QVBoxLayout()
                widget.setLayout(layout)
                scroll_area.setWidget(widget)

            # Get the 'extra_fields' dictionary
            extra_fields = json['extra_fields']

            # Loop through the 'extra_fields' dictionary
            for key, value in extra_fields.items():

                if key not in ["CeramChemID"]:

                    # Create a label and a line edit
                    label = QLabel(key+": ")
                    
                    # Create an input field based on the 'type'
                    if key == "ChemicalSchemaVersion":
                        input_field = QLabel(str(json["__templateversion__"]))
                    elif value['type'] in ['text', 'number']:
                        input_field = QLineEdit(str(value['value']))
                    elif value['type'] == 'select':
                        try:
                            if value['allow_multi_values']:
                                input_field = QWidget()
                                checkbox_layout = QHBoxLayout(input_field)
                                for option in value['options']:
                                    checkbox = QCheckBox(option)
                                    checkbox_layout.addWidget(checkbox)
                            else:
                                pass
                        except:
                            input_field = QComboBox()
                            input_field.addItems(value['options'])
                    elif value['type'] == 'radio':
                        input_field = QComboBox()
                        input_field.addItems(value['options'])
                    elif value['type'] == 'email':
                        input_field = QLineEdit(str(value['value']))
                    elif value['type'] == 'date':
                        input_field = QDateEdit()
                        # Clear the date
                        input_field.clear()
    
                    # Create a horizontal layout and add the label and line edit to it
                    layout = QHBoxLayout()
                    layout.addWidget(label)
                    layout.addWidget(input_field)

                    # Get the 'group_id'
                    group_id = value['group_id']

                    # Get the scroll area for this 'group_id'
                    scroll_area = scroll_areas[group_id - 1]

                    # Get the layout for the scroll area
                    scroll_area_layout = scroll_area.widget().layout()

                    # Add the horizontal layout to the scroll area's layout
                    scroll_area_layout.addLayout(layout)
            
        except:
            pass


    def create_chemicalfromid(self):
        """
        Fetches and stores chemical information for a given chemical ID from the PubChem REST API.

        This function constructs a URL using the chemical ID and other global constants, sends a GET request to that URL, 
        and processes the response. If the request is successful, the function extracts the relevant information from the 
        response and stores it in a global dictionary. If the request fails, the function prints an error message. If the 
        response does not contain the expected data, the function prints a message indicating that no data was found for 
        the given chemical ID.

        Args:
            None

        Returns:
            None
        """
        # Define constants for the REST API
        REST_URL = "https://pubchem.ncbi.nlm.nih.gov/rest"
        DOMAIN = "compound"
        NAMESPACE = "cid"
        # Get the chemical ID from the line edit
        IDENTIFIERS = self.get_lineedit(self.PubChem_lineedit)
        # Define the properties we want to fetch for the compound
        COMPOUND_DOMAIN_INPUTS = ["MolecularFormula", "MolecularWeight", "InChI", "IUPACName", "Title"]
        OUTPUT_SPECIFICATION = "JSON"

        def get_standard_info(compound_domain):
            """
            Fetches standard information for a given compound domain from the PubChem REST API.

            This function constructs a URL using the compound domain and other global constants, sends a GET request to that URL, 
            and processes the response. If the request is successful, the function extracts the relevant information from the 
            response and stores it in a global dictionary. If the request fails, the function prints an error message. If the 
            response does not contain the expected data, the function prints a message indicating that no data was found for 
            the given compound domain.

            Args:
                compound_domain (str): The domain of the compound for which to fetch information.

            Returns:
                None
            """
            # Construct the URL for the GET request
            output_url = f"{REST_URL}/pug/{DOMAIN}/{NAMESPACE}/{IDENTIFIERS}/property/{compound_domain}/{OUTPUT_SPECIFICATION}"
            try:
                # Send the GET request
                response = requests.get(output_url)
                # Raise an exception if the request failed
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                # Print the HTTP error if one occurred
                print(f"HTTP error occurred: {err}")
            except Exception as err:
                # Print any other exceptions that occurred
                print(f"An error occurred: {err}")
            else:
                # Parse the response as JSON
                jsonresponse = response.json()
                try:
                    # Store the relevant information in a global dictionary
                    self.DictionarySelf[compound_domain] = {"Value" : jsonresponse["PropertyTable"]["Properties"][0][compound_domain], "Group": "ChemicalDatasheet"}
                except :
                    # Print a message if no data was found for the given compound domain
                    print("No data for ", compound_domain)

        def get_additional_info():
            """
            Fetches additional information for a given compound from the PubChem REST API.

            This function constructs a URL using global constants, sends a GET request to that URL, 
            and processes the response. If the request is successful, the function extracts the relevant 
            information from the response and stores it in a global dictionary. If the request fails, 
            the function prints an error message. If the response does not contain the expected data, 
            the function prints a message indicating that no data was found.

            Args:
                None

            Returns:
                None
            """
            # Construct the URL for the GET request
            additional_url = f"{REST_URL}/pug_view/data/{DOMAIN}/{IDENTIFIERS}/JSON/?response_type=display"
            
            try:
                # Send the GET request
                response = requests.get(additional_url)
                # Raise an exception if the request failed
                response.raise_for_status()
            except requests.exceptions.HTTPError as err:
                # Print the HTTP error if one occurred
                print(f"HTTP error occurred: {err}")
            except Exception as err:
                # Print any other exceptions that occurred
                print(f"An error occurred: {err}")
            else:
                # Parse the response as JSON
                jsonresponse = response.json()
                # Initialize variables to store GHS hazard and precautionary statements and symbols
                ghs_hazard_statements = ""
                ghs_precautionary_statements = ""
                ghs_symbols = []

                try:
                    # Store the main chemical name in a global dictionary
                    self.DictionarySelf["ChemicalNameMain"] = {"Value" : jsonresponse["Record"]["RecordTitle"], "Group": "ChemicalDatasheet"}
                except:
                    # Print a message if no data was found for the main chemical name
                    print("No data for ChemicalNameMain")

                try:
                    # Store the PubChem CID in a global dictionary
                    self.DictionarySelf["PubchemCID"] =  {"Value" : jsonresponse["Record"]["RecordNumber"], "Group": "ChemicalDatasheet"}
                except:
                    # Print a message if no data was found for the PubChem CID
                    print("No data for PubchemCID")

                # Loop through the sections in the response
                for i, entry in enumerate(jsonresponse["Record"]["Section"]):

                    try:
                        # Check if the section is the "Chemical Safety" section
                        if entry["TOCHeading"] == "Chemical Safety":
                            # Loop through the GHS data in the section
                            for ghs in entry["Information"][0]["Value"]["StringWithMarkup"][0]["Markup"]:
                                # Append the GHS symbol to the list of symbols
                                ghs_symbols.append(ghs["Extra"])
                            # Store the GHS symbols in a global dictionary
                            self.DictionarySelf["GHS"] =  {"Value" : ghs_symbols, "Group": "ChemicalDatasheet"}   
                        
                        # Check if the section is the "Safety and Hazards" section
                        if entry["TOCHeading"] == "Safety and Hazards":
                            # Loop through the sub-sections in the section
                            for subentry in entry["Section"]:
                                # Check if the sub-section is the "Hazards Identification" sub-section
                                if subentry["TOCHeading"] == "Hazards Identification":
                                    # Loop through the sub-sub-sections in the sub-section
                                    for subsubentry in subentry["Section"]:
                                        # Check if the sub-sub-section is the "GHS Classification" sub-sub-section
                                        if subsubentry["TOCHeading"] == "GHS Classification":
                                            # Loop through the sub-sub-sub-sections in the sub-sub-section
                                            for subsubsubentry in subsubentry["Information"]:
                                                # Check if the sub-sub-sub-section is the "GHS Hazard Statements" sub-sub-sub-section
                                                if subsubsubentry["Name"] == "GHS Hazard Statements":
                                                    # Check if the GHS hazard statements have not been initialized
                                                    if ghs_hazard_statements == "":
                                                        # Loop through the hazard statements in the sub-sub-sub-section
                                                        for Hstatement in subsubsubentry["Value"]["StringWithMarkup"]:
                                                            # Append the hazard statement to the GHS hazard statements
                                                            ghs_hazard_statements += Hstatement["String"].replace("[", "").replace("]", "") + "; "
                                                # Check if the sub-sub-sub-section is the "Precautionary Statement Codes" sub-sub-sub-section
                                                if subsubsubentry["Name"] == "Precautionary Statement Codes":
                                                    # Check if the GHS precautionary statements have not been initialized
                                                    if ghs_precautionary_statements == "":
                                                        # Loop through the precautionary statements in the sub-sub-sub-section
                                                        for Pstatement in subsubsubentry["Value"]["StringWithMarkup"]:
                                                            # Check if the precautionary statement is the end of the list
                                                            if "(The corresponding statement to each P-code" in Pstatement["String"]:
                                                                # Break the loop if the end of the list has been reached
                                                                break
                                                            # Append the precautionary statement to the GHS precautionary statements
                                                            ghs_precautionary_statements += Pstatement["String"].replace("[", "").replace("]", "").replace(",", ";").replace("and ", "") + "; "
                                                            
                            # Store the GHS hazard statements in a global dictionary
                            self.DictionarySelf["GHSHazardStatements"] = {"Value" : ghs_hazard_statements, "Group": "ChemicalDatasheet"}
                            # Store the GHS precautionary statements in a global dictionary
                            self.DictionarySelf["PrecautionaryStatements"] = {"Value" : ghs_precautionary_statements, "Group": "ChemicalDatasheet"}

                    except:
                        # Print a message if no data was found for GHS
                        print("No data for GHS")

                    # Try block to handle potential exceptions
                    try:
                        # Check if the section is the "Names and Identifiers" section
                        if entry["TOCHeading"] == "Names and Identifiers":
                            # Loop through the identifiers in the section
                            for identifier in entry["Section"]:
                                # Check if the identifier is the "Record Description" identifier
                                if identifier["TOCHeading"] == "Record Description":
                                    # Loop through the record identifiers in the identifier
                                    for record_identifier in identifier["Information"]: 
                                        # Check if the record identifier is the "Physical Description" record identifier
                                        if record_identifier["Description"] == "Physical Description":
                                            # Store the physical description in a global dictionary
                                            self.DictionarySelf["PhysicalDescription"] = {"Value" : record_identifier["Value"]["StringWithMarkup"][0]["String"], "Group": "ChemicalDatasheet"}
                                            # Break the loop after storing the physical description
                                            break

                                # Check if the identifier is the "Other Identifiers" identifier
                                elif identifier["TOCHeading"] == "Other Identifiers":
                                    # Loop through the other identifiers in the identifier
                                    for other_identifier in identifier["Section"]:                                
                                        # Check if the other identifier is the "CAS" other identifier
                                        if other_identifier["TOCHeading"] == "CAS":
                                            # Store the CAS number in a global dictionary
                                            self.DictionarySelf["CAS"] = {"Value" : other_identifier["Information"][0]["Value"]["StringWithMarkup"][0]["String"], "Group": "ChemicalDatasheet"}
                                            # Break the loop after storing the CAS number
                                            break  

                    # Exception handling block
                    except Exception as e:
                        # Print the exception if one occurred
                        print(e)  

        # Call the seperate info functions.
        for compound_domain in COMPOUND_DOMAIN_INPUTS:
            get_standard_info(compound_domain)
        get_additional_info()


    def fill_chemdatabase_from_dict(self, scroll_areas):
        """
        Fills the widgets in the provided scroll areas with data from the instance's DictionarySelf attribute.

        This function iterates over each scroll area provided. For each scroll area, it retrieves the layout and 
        iterates over each item in the layout. It checks the type of each widget in the layout and sets its value 
        based on the corresponding value in DictionarySelf.

        Parameters:
        scroll_areas (list): A list of QScrollArea objects to be filled with data.

        """

        for scrollarea in scroll_areas:
            widget = scrollarea.widget()
            layout = widget.layout()
            for i in range(layout.count()):
                hbox_layout = layout.itemAt(i)

                if hbox_layout is not None:  # Check if the layout item is a layout
                    widget1 = hbox_layout.itemAt(0).widget()
                    widget2 = hbox_layout.itemAt(1).widget()

                try:
                    if isinstance(widget2, QLabel):
                        widget2.setText(str(self.DictionarySelf[widget1.text().split(":")[0]]["Value"]))
                    elif isinstance(widget2, QLineEdit):
                        widget2.setText(str(self.DictionarySelf[widget1.text().split(":")[0]]["Value"]))
                    elif isinstance(widget2, QWidget):

                        checkboxes = widget2.findChildren(QCheckBox,"", Qt.FindChildrenRecursively)
                        for checkbox in checkboxes:
                            print(checkbox.text())
                            if checkbox.text() in self.DictionarySelf[widget1.text().split(":")[0]]["Value"]:
                                checkbox.setChecked(True)
                            else:
                                checkbox.setChecked(False)

                except:
                    pass
        
        self.filledbypubchem = True

    def chemicalinfo_to_json(self, scroll_areas):

        self.chemjson = chemicaltemplate

        for scrollarea in scroll_areas:
            widget = scrollarea.widget()
            layout = widget.layout()
            for i in range(layout.count()):
                hbox_layout = layout.itemAt(i)

                if hbox_layout is not None:  # Check if the layout item is a layout
                    widget1 = hbox_layout.itemAt(0).widget()
                    widget2 = hbox_layout.itemAt(1).widget()

                try:
                    if isinstance(widget2, QLabel):
                        pass

                    elif isinstance(widget2, QLineEdit):
                        self.chemjson["extra_fields"][widget1.text().split(":")[0]]["value"] = widget2.text()

                    elif isinstance(widget2, QDateEdit):
                        if widget2.date().toString("yyyy-MM-dd") == "2000-01-01":
                            self.chemjson["extra_fields"][widget1.text().split(":")[0]]["value"] = ""
                        else:
                            self.chemjson["extra_fields"][widget1.text().split(":")[0]]["value"] = widget2.date().toString("yyyy-MM-dd")
                    elif isinstance(widget2, QWidget):
                        try:
                            if self.chemjson["extra_fields"][widget1.text().split(":")[0]]["allow_multi_values"]:
                                checkboxes = widget2.findChildren(QCheckBox,"", Qt.FindChildrenRecursively)
                                val = [] 
                                for checkbox in checkboxes:
                                    if checkbox.isChecked():
                                        val.append(checkbox.text())
                                    else:
                                        pass
                            else:
                                pass
                        except:
                            self.chemjson["extra_fields"][widget1.text().split(":")[0]]["value"] = widget2.currentText()           
                except:
                    pass

                try:
                    self.chemjson["extra_fields"]["ChemicalSchemaVersion"]["value"] = self.chemjson["__templateversion__"]
                except:
                    pass
        
        print(self.chemjson)


    def chemid_to_elabftw(self):

        if self.chemjson != "":

            if self.filledbypubchem:
                self.chemjson["extra_fields"]["PubchemDisclaimer"] = {"type": "text", "value": "Some data was fetched from Pubchem and should be verified/handled with caution.", "description": "Disclaimer for PubChem data", "group_id": 1, "readonly": True}
                

            # These lines configure the eLabFTW API client using the provided API key and base URL. It also sets additional configurations, such as disabling SSL verification and debugging.
            configuration = elabapi_python.Configuration()
            configuration.api_key['api_key'] = configdict["API_Key"]
            configuration.api_key_prefix['api_key'] = 'Authorization'
            configuration.host = configdict["ElabFTW_URL"]
            configuration.debug = False
            configuration.verify_ssl = False

            # This creates an instance of the eLabFTW API client (api_client) with the specified configuration. It also fixes an issue related to the Authorization header not being properly set by the generated library.
            api_client = elabapi_python.ApiClient(configuration)
            api_client.set_default_header(header_name='Authorization', header_value=configdict["API_Key"])

            # This line initializes the ItemsApi class using the configured API client. It provides an interface for working with eLabFTW items.
            itemsApi = elabapi_python.ItemsApi(api_client)

            # Disable SSL warnings
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # This section demonstrates creating a new item with the specified category and tags. It then retrieves the newly created item's ID from the response and modifies its title, body, and rating.
            targetCategory = configdict["Chem_ID"]
            tags = [self.chemjson["extra_fields"]["ChemicalNameMain"]["value"], self.chemjson["extra_fields"]["IUPACName"]["value"], self.chemjson["extra_fields"]["CAS"]["value"], self.chemjson["extra_fields"]["PubchemCID"]["value"]]
            response = itemsApi.post_item_with_http_info(body={'category_id': targetCategory, 'tags': tags})
            locationHeaderInResponse = response[2].get('Location')
            itemId = int(locationHeaderInResponse.split('/').pop())

            # Add the CeramChemID to the metadata
            self.chemjson["extra_fields"]["CeramChemID"]["value"] = "CHEM" + str(itemId)

            # Update the item with the CeramChemID and extra fields.
            title = self.chemjson["extra_fields"]["CeramChemID"]["value"] + " - " + self.chemjson["extra_fields"]["ChemicalNameMain"]["value"]
    
            itemsApi.patch_item(itemId, body={'title': title, 'body': "", "metadata" : json.dumps(self.chemjson)})

            # Log
            self.create_log("Saved Chemical to elabFTW at: " + locationHeaderInResponse)
            self.set_label(self.AddChemicalResponse_label, "Created chemical with ID: " + self.chemjson["extra_fields"]["CeramChemID"]["value"])

        else:
            self.create_log("No chemical data available.")
                
####################################################################################################################################
####################################################################################################################################


# Run the program.
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        win = Gui()
        win.show()
        sys.exit(app.exec())
    except Exception as a:
        errorpath = os.path.join(outputfolder, "errorlog.txt")
        f = open(errorpath, "a")
        f.write(str(a) + "\n")
        f.close()