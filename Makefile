.PHONY: install-uv test
install-uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv python install 3.14

test:
	cd ./mediaboard_task && uv run -m pytest

dev:
	cd ./mediaboard_task && uv run manage.py runserver

docker:
	docker compose up --build