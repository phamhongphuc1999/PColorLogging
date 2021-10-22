build:
	python3 -m build

upload:
	python3 -m twine upload dist/*

update:
	python3 -m twine upload --skip-existing dist/*

install:
	python3 -m pip install --upgrade twine
	python3 -m pip install --upgrade build
