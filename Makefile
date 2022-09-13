install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:	
	black *.py mylib/*.py

refactor: format lint

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

all: install lint test