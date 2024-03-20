# elabScan
This project is intended to provide a software for creating sampleIDs, which can be printed as QR code, saved as a PNG or uploaded into the electronic laboratory notebook "elabFTW". The program was originally programmed under the name "CeramScan" at the Chair of Advanced Ceramic Materials at the Technische Universität Berlin. It will be adapted soon(TM) to be under the name elabScan.

## Installation

Under construction

### Config.txt

Make sure to create a file in your main directory called "config.txt" or rename the "config_example.txt".

It should be in the format of:

```
API_Key = XYZ
Category_ID = 1
ElabFTW_URL = https://xyz/api/v2/
Institution = YOUR INSTITUTE
StartingYear = 2011
Standard Output folder = 
LinkID = https://xyz
```

* API Key is the key you can create with elabFTW. It should have Read/Write access.
* Category ID is the id of the database/resource element that you create. E.g., the sampleID database element that you created before.
* ElabFTW URL is the link to your elabftw installation.
* Institution is the name of your workplace.
* Starting year is the year from which the CeramScan program counts upwards.
* Link ID is the link to your excel table which has the first, last names and their abbreviation present. Currently it reaches a tubcloud Excel file with a worksheet called "userid".

## More information
[See the Wiki for more information](https://git.tu-berlin.de/ceramics/ceramscan-development/ceramscan/-/wikis/home)

## Support
In case of questions, comments or bug reports open an Issue.

## Roadmap
Under construction

## Contributing
Under construction

## License
Under construction

## Project status
Healthy and running!
