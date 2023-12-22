PROJECT=mammograms
PYTHON=pdm run python
CODE_DIRS=$(PROJECT) tests util
LINE_LEN=120

style:
	$(PYTHON) -m autoflake -r -i $(CODE_DIRS)
	$(PYTHON) -m isort $(CODE_DIRS)
	$(PYTHON) -m autopep8 -a -r -i $(CODE_DIRS)
	$(PYTHON) -m black $(CODE_DIRS)

quality:
	$(PYTHON) -m black --check $(CODE_DIRS)
	$(PYTHON) -m autopep8 -a $(CODE_DIRS) 

node_modules:
	npm install

types: node_modules
	pdm run npx --no-install pyright tests $(PROJECT)

test:
	$(PYTHON) -m pytest -s -v tests --cov=./$(PROJECT) --cov-report=xml
 
check:
	$(MAKE) style
	$(MAKE) quality
	$(MAKE) types
	$(MAKE) test

clean:
	rm -rf node_modules \
		env \
		*.egg-info \
		__pycache__ \
		.pytest_cache

clean-venv:
	pdm venv remove -y $(PROJECT)

reset:
	$(MAKE) clean
	$(MAKE) clean-venv
	$(MAKE) init
	$(MAKE) check

init: pdm.lock
	which pdm || pip install --user pdm
	pdm venv create -n $(PROJECT)
	pdm sync -d

pdm.lock:
	$(MAKE) update

update:
	pdm lock
	pdm install -d

circleci:
	circleci config validate 
	circleci local execute test
