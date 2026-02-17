# secret-santa

# Development
## Dependencies
### Python Environment
With an ".venv/" created and activated, install the dependencies with:
```
pip install -e ".[dev]"
```
### Migrations
First time you deploy you need to initializate the database by running the migration scripts from the container:
```
docker compose -f docker-compose.dev.yaml exec -it web bash
cd src/
python manage.py migrate
```

## Run the proyect
```
docker compose -f docker-compose.dev.yaml up --build
```

### Tailwind
To have refreshing on the fly tailwind, watching for changes in the templates you have to run:
```
npm install && npx @tailwindcss/cli -i ./src/static/src/input.css -o ./src/static/src/output.css --watch
```