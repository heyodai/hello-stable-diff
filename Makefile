####################
# Makefile for the project
#
# @see: https://earthly.dev/blog/python-makefile/
####################


# Initialize the project and create the virtual environment
#
# The odd syntax is to ensure that the virtual environment is
# created before the requirements are installed.
#
# @see https://stackoverflow.com/questions/74737897/
# (Yes, that's my own Stack Overflow question :P)
env:
	\
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \


# Run the project
#
# This will run the project in the virtual environment
picture:
	source venv/bin/activate; \
	python3 main.py; \

# Automatically reinstall dependencies when requirements.txt changes
#
# This will trigger when venv is activated.
venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt


# Clean up the cache and virtual environment
# Run this if you are having issues with the project
# or if you want to start fresh
#
# After running this, you will need to run `make env` again
clean:
	rm -rf __pycache__
	rm -rf venv