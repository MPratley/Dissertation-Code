On ubuntu you'll need to install venv and pip from the system repos:
```
sudo apt-get install python3-venv python3-pip
```

While technically optional, I highly recommend making a venv for this project in the `./.venv/` folder

```
python3 -m venv .venv
```

Remember to activate it too!

```
source .venv/bin/activate
```

(Sourcing only works on bash or zsh, not fish (understandably as fish has completely different syntax) )

Finally, pull in the required dependencies. 

```
pip install -r requirements.txt
# ^You don't to use pip3 as this is already a python3 venv. Magic!
```

to update them, DON'T DO a freeze.
```
# none of this please : (
# pip freeze > requirements.txt
```
Just add the top level deps you actually intend on installing. Keeping requirements.txt files in a readable state is more important than capturing the exact non-top-level deps you may use (<- opinion).
