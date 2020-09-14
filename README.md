# Equal Rights for All (Conde Nast 2020 Hackathon Entry)  

## Participants  
Max Cantor, Parameswaran Kandasamy, Charlene Luo, Michele Tram  

### How to use  
* Clone / fork this repo  
* Make sure you have python and pip (tested only with a conda environment)  
* Install requirements: `pip install -r requirements.txt`  
* Install ERA package: run `./build_sh` to build a python wheel distribution, or `pip install -e .`  
* Create `constants_example.yml` in the main directory, modeled after `constants_example.yml`, with your NYC Open Data information, Google information, and the path for your NYPD Complaint data (e.g. `NYPD_Complaint_DB/CCRB_database_raw.csv` for the raw csv database in the NYPD_Complaint_DB directory)  

### Description  
Creates normalized class structures for various offline datasets (e.g. `NYPDComplaints`) and online data sources (e.g. `NYCODAPIClient`)  
