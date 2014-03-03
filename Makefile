PYTHONPATH := "$(PYTHONPATH):$(PWD)" 
export PYTHONPATH

serve:
	@echo $(shell echo '$$PYTHONPATH')
	./bin/_

test:
	nosetests-3.3
