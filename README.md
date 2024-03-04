# Coverage Calculation in TestRail

Calculating coverage of automation test cases in each project in TestRails using TestRail APIs

## Pre-requisites

* Ensure that python version > 3 is installed in your system. You can download latest version from [here](https://www.python.org/downloads/)

## Setup

* Clone Test-Coverage-Calculation repository using following command:
```
git clone git@github.com:mahnoorfatiima/Test-Coverage-Calculation.git
```

* Run below commmand to install `requests` package:
```
pip3 install requests
```

* Run the coverageCalculation.py file and wait for the script to complete:
```
python3 coverageCalculation.py
```

**NOTE:**

Before running this project: 

* Update project names and IDs in projects.py according to your TestRail projects
* Update sub domain in API URL and TestRail credentials in coverageCalculation.py

Below is the link to the all useful APIs:
  - [Suites – TestRail Support Center](https://support.testrail.com/hc/en-us/articles/7077936624276-Suites#getsuite)
  - [Cases – TestRail Support Center](https://support.testrail.com/hc/en-us/articles/7077292642580-Cases#getcases)
  - [Tests – TestRail Support Center](https://support.testrail.com/hc/en-us/articles/7077990441108-Tests#gettest)
  - [Runs – TestRail Support Center](https://support.testrail.com/hc/en-us/articles/7077874763156-Runs#getrun)
