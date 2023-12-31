﻿# Kookkelder API
As software developers at Gilde DevOps Solutions, we are tasked with developing one or more applications for managing and recording ingredients and recipes. This project addresses the need for a smart inventory system, similar to what we find in refrigerators, to efficiently manage ingredients and recipes in various settings.

## Installation

### Create a new virtual environment:
```
python -m venv venv
```
After running the above command, a new folder named "venv" will be created. 
Then you should restart your IDE.

### Install dependencies:
```
pip install -r requirements.txt
```

### Create a database name "kookkelder" in MySQL and then run the following migration command:
```
flask db upgrade
```

### Run the server:
```
python app.py
```
