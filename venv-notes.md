
# setup virtual environment folder location, example as below
export VENV="${HOME}/venv"

# Python3
### creating python3 virtual environment in the directory $PWD/py3
```
python3 -m venv ${VENV}/py3
```

# activating  and deactivating python3 virtual environment
```
source ${VENV}/py3/bin/activate
deactivate
```


# Python2
### creating python2 virtual environment in the directory $PWD/py2
```
virtualenv -p /usr/bin/python2 ${VENV}/py2
```

### activating python2 virtual environment
```
source ${VENV}/py2/bin/activate
deactivate
```

