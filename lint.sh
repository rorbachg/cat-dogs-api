#!/usr/bin/env bash

set -e
set -x

ruff check .
black . --check --diff
isort . --check-only --diff