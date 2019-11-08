# mini_flask_app

### To run the app: 

Create and initialize a virtual env: 

```
virtualenv .env-stitch-test

. .env-stitch-test/bin/activate
```

### Install requirements

```
pip install -r requirements.txt
```

We're using flask, so we have to tell flask that we want it to read main: 

```
export FLASK_APP=main.py
```

To run the app, choose either: 

```
python main.py
```

for 'debug mode' or

```
flask run
```

Navitage to `localhost:5000/vat/<country_code>` to see country-specific VAT 

