# 
# 
# 

.PHONY: fmt lint

fmt: install
	poetry run black ${FMT_DIRS}
	poetry run isort ${FMT_DIRS}
	poetry run docformatter --in-place -r ${FMT_DIRS}

lint: install
	poetry run black --check ${FMT_DIRS}
	poetry run isort --check-only ${FMT_DIRS}
	poetry run docformatter --check -r ${FMT_DIRS}
	