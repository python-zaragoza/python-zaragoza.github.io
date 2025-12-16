include .environment/makefile
include .makefiles/development.mk
include .makefiles/printing.mk

.PHONY: run
run:
	@$(call pinfo,Running the project...)
	uv run reflex run

run-front:
	@$(call pinfo,Running the project in frontend-only mode...)
	uv run reflex run --frontend-only

build:
	uv run reflex export

build-front:
	uv run reflex export --frontend-only

build-raw:
	uv run reflex export --no-zip

build-front-raw:
	uv run reflex export --frontend-only --no-zip

fetch-meetup:
	@$(call pinfo,Fetching events from Meetup.com...)
	uv run python scripts/fetch_meetup.py
