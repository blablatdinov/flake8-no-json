# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run mypy flake8_no_json tests/**/*.py
	poetry run flake8 .

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check

.PHONY: test
test: lint package unit

.DEFAULT:
	@cd docs && $(MAKE) $@

