# ALS DataEngineer Assessment
ALS Hiring Data Engineer Extract Transform Load (ETL) exercise to manipulate and aggregate large datasets with pandas.

- [ALS DataEngineer Assessment](#als-dataengineer-assessment)
  - [Download](#download)
  - [Using etl_jupyternb.ipynb](#using-etl_jupyternbipynb)
  - [Using etl_script.py](#using-etl_scriptpy)
  - [Requirements](#requirements)
  - [Install dependencies](#install-dependencies)
  - [Run script](#run-script)
- [Increasing speed](#increasing-speed)


This repository contains two files to run the ETL exercise:
  1. **etl_jupyternb.ipynb**: a [jupyter notebooks](https://github.com/jupyter/notebook) that contains all documentation, additional exploratory data analysis, and produces the output files.
  2. **etl_script.py**: python script that can be run via the terminal to produce the output files.


## Download 
This repository can be downloaded from GitHub via:

```
git clone https://github.com/{}/ALS_Assessment.git
```
*Note: removed owner name to preserve anonymity.*


## Using etl_jupyternb.ipynb
If you have Jupyter Notebooks installed, you can access the **etl_jupyternb.ipynb** locally. Otherwise, [NBViewer.org](http://nbviewer.org) renders a GitHub Jupyter Notebook online. 


## Using etl_script.py
_Note:_ This section assumes you are using Windows OS.


## Requirements
Python version 3.6+

3rd party libraries documented in requirements.txt
- numpy
- matplotlib
- pandas 
- seaborn
- missingno
- pywrangle


## Install dependencies
To run this script, you must install the dependencies outlined in the requirements.txt file. I recommend using a virtual environment to manage these dependencies. Learn more [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

To install the dependencies with a virtual environment, navigate to the directory for the cloned repository and run 
```
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
deactivate
```

## Run script
After the dependencies have been installed, you can run the the etl_script.py from the command line using:

```
venv\Scripts\active
python etl_script.py
deactivate
```

# Increasing speed
If you would like to increase the speed of the scripts, download the following csvs and place them in the same working directory as the script:
1. [Constituent Information](https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv)
2. [Constituent Email Addresses](https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv)
3. [Constituent Subscription Status](https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv)

