
# Setup virtual environment folder location, example as below
export VENV="${HOME}/venv"

# Python3
#### Creating python3 virtual environment in the directory $PWD/py3
```
python3 -m venv ${VENV}/py3
```

#### Activating  and De-activating python3 virtual environment
```
source ${VENV}/py3/bin/activate
deactivate
```


# Python2
#### Creating python2 virtual environment in the directory $PWD/py2
```
virtualenv -p /usr/bin/python2 ${VENV}/py2
```

#### Activating  and De-activating python2 virtual environment
```
source ${VENV}/py2/bin/activate
deactivate
```
