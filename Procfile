web: gunicorn app:app
release: export FLASK_APP="run.py"
export APP_SETTINGS="development"
export JWT_SECRET_KEY ="JWT_SECRET_KEY"
export DATABASE_URL="postgresql://localhost/flask_api"
python run.py