To make a venv:

`python3 -m venv venv`

To source it

`source venv/bin/activate`

Sourcing only works on bash or zsh, not fish (understandably as fish has completely different syntax)

to pull in deps

`pip install -r requirements.txt`

to update them

DONT DO `pip freeze > requirements.txt`
Just add the top level deps you actually intend on installing