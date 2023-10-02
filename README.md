# Kookkelder API

## Installation

### Create a new virtual environment:
```
python -m venv venv
```

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
