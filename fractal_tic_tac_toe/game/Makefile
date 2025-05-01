TEST = pytest
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
COVERAGE = python -m pytest
DOCUMENTATION = pdoc
DOCUMENT_ARGS = -o ./fractal_tic_tac_toe/docs/

.PHONY: all
all: check-style check-type run-test-coverage
	@echo "All checks passed"

.PHONY: check-type
check-type:
	$(TYPE_CHECK) ./

.PHONY: check-style
check-style:
	$(STYLE_CHECK) ./

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) ./tests


.PHONY: run-test-coverage
run-test-coverage:
	$(COVERAGE) -v --cov-report=html:./htmlcov --cov-report=term --cov=./ ./tests

.PHONY: docs
docs:
	$(DOCUMENTATION) $(DOCUMENT_ARGS) ./*.py

.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -name .coverage` # remove all coverage cache 
	rm -rf `find . -type d -name docs` # remove all generated documents
