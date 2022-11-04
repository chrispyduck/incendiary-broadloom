.PHONY: clean rebuild

rebuild: clean bomber 

clean:
	rm -f requirements.txt bomber 

requirements.txt:
	poetry run pip freeze > requirements.txt

bomber: requirements.txt
	poetry run pex -r requirements.txt -o bomber -v --sources-directory=. --entry-point src.main:main
	