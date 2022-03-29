clean:
	@rm -rf encounter.venv

bootstrap:
	make clean
	@python3.10 -m venv encounter.venv
	@encounter.venv/bin/python -m pip install --upgrade pip
	@encounter.venv/bin/python -m pip install dice==3.1.2

encounter:
	@encounter.venv/bin/python encounter.py
