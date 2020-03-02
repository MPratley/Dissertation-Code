To make a venv:

`python3 -m venv venv`

To source it

`source venv/bin/activate`

Sourcing only works on bash or zsh, not fish (understandably as fish has completely different syntax)

to pull in deps

`pip install -r requirements.txt`

to update them

`pip freeze > requirements.txt`

(yes, freeze is generally bad, this should probably be a real deps list.)