

class Gui_GetSet():
    """
    Main class for creating class specific functions. MainLabelCreate, CharLabelCreate and ChemLabelCreate inherit these functions.
    Functions:
    """
    def __init__(self):
        """
        INIT Method
        """
        pass

    def tabchange(self, tabobject, index):
        """
        Set the current index of a tab object.

        Parameters:
        - tabobject: The tab object.
        - index (int): The index to set for the tab.

        Returns:
        None
        """
        tabobject.setCurrentIndex(index)


    def set_label(self, labelobject, labeltext):
        """
        Sets the text of a label object.

        Parameters:
        - labelobject: The label object.
        - labeltext (str): The text to set for the label.

        Returns:
        None
        """
        labelobject.setText(labeltext)

    
    def get_lineedit(self, lineeditobject, upper = True):
        """
        Gets the text of a line edit object. Optionally updates the text to be uppercase.

        Parameters:
        - lineeditobject: The line edit object.
        - upper (bool): If True, converts the text to uppercase.

        Returns:
        str: The text of the line edit object.
        """
        lineedittext = lineeditobject.text()

        if upper:
            lineedittext= lineedittext.upper()
            lineeditobject.setText(lineedittext)
        
        return lineedittext


    def set_lineedit(self, lineeditobject, input):
        """
        Sets the text of a line edit object.

        Parameters:
        - lineeditobject: The line edit object.
        - input (str): The text to set for the line edit.

        Returns:
        None
        """
        lineeditobject.setText(input)

    
    def upper_lineedit(self, lineeditobject):
        """
        Sets the text of a line edit object to uppercase.

        Parameters:
        - lineeditobject: The line edit object.

        Returns:
        None
        """
        lineedittext = lineeditobject.text()
        lineedittext= lineedittext.upper()
        lineeditobject.setText(lineedittext)


    def get_date(self, dateobject):
        """
        Gets a date from a date time object and splits it into Year, Month, Day.

        Parameters:
        - dateobject: The date time object.

        Returns:
        Tuple[int, int, int]: Year, Month, Day
        """
        date = dateobject.date().toPython()
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")

        return int(year),int(month),int(day)
    

    def set_date(self, dateobject, dateinput):
        """
        Sets the date value in the specific date field.

        Parameters:
        - dateobject: The date object.
        - dateinput: The date to set.

        Returns:
        None
        """
        dateobject.setDate(dateinput)


    def encrypt_year(self, encryptyear, startingyear):
        """
        Translates a year to an alphanumeric character.

        Parameters:
        - encryptyear (int): The year to be translated.
        - startingyear (int): The starting year for translation.

        Returns:
        str: The translated alphanumeric character representing the year.
        """
        shortyear = chr(int(encryptyear)-startingyear+65)

        return shortyear
    

    def decrypt_year(self, decryptyear, startingyear):
        """
        Translates alphanumeric characters to a year.

        Parameters:
        - decryptyear (str): The alphanumeric character representing the year.
        - startingyear (int): The starting year for the translation.

        Returns:
        int: The translated year.

        Raises:
        TypeError: If the input is not in the correct format.
        """
        if isinstance(decryptyear, str) and len(decryptyear) == 1 and decryptyear.isalpha():
            year = int(ord(decryptyear.upper())) + startingyear - 65
            return year
        else:
            raise TypeError("Input must be a letter.")


    def encrypt_month(self, encryptmonth):
        """
        Translates a month to an alphanumeric character.

        Parameters:
        - encryptmonth (int): The month to be translated.

        Returns:
        str: The translated alphanumeric character representing the month.
        """
        shortmonth = chr(int(encryptmonth)-1+65)
        return shortmonth
    

    def decrypt_month(self, decryptmonth):
        """
        Translates alphanumeric characters to a month.

        Parameters:
        - decryptmonth (str): The alphanumeric character representing the month.

        Returns:
        int: The translated month.

        Raises:
        TypeError: If the input is not in the correct format.
        """ 
        if isinstance(decryptmonth, str) and len(decryptmonth) == 1 and decryptmonth.isalpha():
            month = int(ord(decryptmonth.upper())) + 1 - 65
            return month
        else:
            raise TypeError("Input must be a letter.")


    def encrypt_day(self, encryptday):
        """
        Translates a day to an alphanumeric character.

        Parameters:
        - encryptday (int): The day to be translated.

        Returns:
        str or int: The translated alphanumeric character or integer representing the day.
        """
        if int(encryptday) <= 26:
            shortday = chr(int(encryptday)-1+65)
        else:
            shortday = int(encryptday) - 26

        return shortday


    def decrypt_day(self, decryptday):
        """
        Translates alphanumeric characters to a day.

        Parameters:
        - decryptday (str or int): The alphanumeric character or integer representing the day.

        Returns:
        int: The translated day.

        Raises:
        TypeError: If the input is not in the correct format.
        """
        try:
            if int(decryptday) <= 5:
                day = int(decryptday) + 26
            else:
                raise TypeError("Wrong format for the day.")
        except:
            if isinstance(decryptday, str) and len(decryptday) == 1 and decryptday.isalpha():
                day = int(ord(decryptday.upper())) + 1 - 65
            else:
                raise TypeError("Wrong format for the day.")
        return day


    def getstate_checkbox(self, checkboxobject):
        """
        Get the state of a checkbox.

        Parameters:
        - checkboxobject: The checkbox object.

        Returns:
        bool: True if the checkbox is checked, False otherwise.
        """
        if checkboxobject.isChecked():
            return True
        else:
            return False


    def checkbox_visibilitychange(self, checkboxobject, visibleobject, inverse = False):
        """
        Set the visibility of an object according to the state of a checkbox object.

        Parameters:
        - checkboxobject: The checkbox object.
        - visibleobject: The object whose visibility is controlled by the checkbox.
        - inverse (bool): If True, the visibility is set inversely to the checkbox state.

        Returns:
        bool: The new visibility state of the object.

        Note:
        If inverse is True, the object's visibility will be set to False when the checkbox is checked,
        and vice versa.
        """
        if inverse:
            if checkboxobject.isChecked():
                visibleobject.setVisible(False)
                return False
            else:
                visibleobject.setVisible(True)
                return True

        else:
            if checkboxobject.isChecked():
                visibleobject.setVisible(True)
                return True
            else:
                visibleobject.setVisible(False)
                return False
