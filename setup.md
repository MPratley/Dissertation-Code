On ubuntu:
```
sudo apt-get install python3-venv python3-pip
```

To make a venv:

```
python3 -m venv venv
```

To source it

```
source venv/bin/activate
```

Sourcing only works on bash or zsh, not fish (understandably as fish has completely different syntax)

to pull in deps

```
pip install -r requirements.txt
```

to update them

DON'T DO 
```
#pip freeze > requirements.txt
```
Just add the top level deps you actually intend on installing