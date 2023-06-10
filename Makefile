py := poetry run
package_dir := app
tests_dir := tests

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: run
run: ## Run app
	$(py) python -m $(package_dir).api

.PHONY: generate
generate: ## Generate alembic migration (args: name="Init")
	alembic revision --m="${name}" --autogenerate

.PHONY: migrate
migrate: ## Migrate to new revision
	alembic upgrade head


.PHONY: run
run: ## Run app
	$(py) python -m $(package_dir)