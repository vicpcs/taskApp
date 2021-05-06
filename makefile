init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	python3 ./taskApp/app.py

.PHONY: init test
