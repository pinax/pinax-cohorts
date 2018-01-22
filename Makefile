all: init docs test

init:
	python setup.py develop
	pip install detox coverage

test:
	coverage erase
	detox
	coverage html
