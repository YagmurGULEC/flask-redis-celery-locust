SHELL=./make-venv
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1


install:
	python3 -m venv venv
	pip install --upgrade pip

post-install:
	pip install -r requirements.txt

run:
	flask run




