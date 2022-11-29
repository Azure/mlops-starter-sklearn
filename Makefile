env-create:
	conda env create --prefix=.venv --file=environments/environment.yml
env-update:
	conda env update --prefix=.venv --file=environments/environment.yml