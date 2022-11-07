env-create:
	conda env create --prefix=.env --file=environments/environment.yml
env-update:
	conda env update --prefix=.env --file=environments/environment.yml