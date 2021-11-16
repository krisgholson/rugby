# rugby
Code and scripts to make managing rugby data a little bit easier.

## setup
Use pyenv to manage python version and virtual environments. See https://realpython.com/intro-to-pyenv/

```
# creating the virtualenv
pyenv virtualenv 3.8.10 rugby

# using it
pyenv local rugby 
pyenv activate rugby

# install dependencies
pip install -r requirements.txt
```

## running
```bash
python sportlomo/members.py
```

## deploy the web services

one-time setup for domain
```bash
sls create_domain --stage prod --aws-profile lowcountry_rugby
```

```bash
sls client deploy --stage prod --aws-profile lowcountry_rugby
sls deploy --stage prod --aws-profile lowcountry_rugby
```
