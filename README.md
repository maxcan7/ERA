# Equal Rights for All (Conde Nast 2020 Hackathon Entry)  

## Participants  
Max Cantor, Parameswaran Kandasamy, Charlene Luo, Michele Tram  

### How to use  
* Clone / fork this repo  
* Make sure you have python and pip (tested only with a conda environment)  
* Install requirements: `pip install -r requirements.txt`  
* Install ERA package: run `./build_sh` to build a python wheel distribution, or `pip install -e .`  
* Create `constants.yml` in the main directory, modeled after `constants_example.yml`, with your NYC Open Data information, Google information, and the path for your NYPD Complaint data (e.g. `NYPD_Complaint_DB/CCRB_database_raw.csv` for the raw csv database in the NYPD_Complaint_DB directory)  
* The classes can be passed a constants dict as a keyword argument rather than expecting one in the directory  
* The NYPD Complaints data can be read from dbfs rather than from local files  

### Requirements  
In addition to the python package requirements in requirements.txt, this package has the following requirements:  
* python  
* a databricks account  
* a New York Open Data account and app token  
* a local copy or dbfs uploaded copy of the NYPD Misconduct Complaint Database: https://github.com/new-york-civil-liberties-union/NYPD-Misconduct-Complaint-Database  

### Description  
Creates normalized class structures for various offline datasets (e.g. `NYPDComplaints`) and online data sources (e.g. `NYCODAPIClient`)  
