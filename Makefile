build:
	mkdocs build

serve:
	mkdocs serve

deploy:
	mkdocs gh-deploy --config-file mkdocs.yml --remote-branch gh-pages