env-create:
	conda env create --prefix=.env --file=environment.yml
env-update:
	conda env update --prefix=.env --file=environment.yml