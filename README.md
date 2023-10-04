# Kookkelder API

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
