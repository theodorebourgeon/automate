# Try to automate things

Activate virtual env
`export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3`
`source /usr/local/bin/virtualenvwrapper.sh`
`workon automate`
Desactivate env
`deactivate`

Install env
`pip install -r requirements.txt`

Run
`python main.py`

Save new requirements
`pip freeze > requirements.txt`
