install: from requirements.txt
fastapi
uvicorn[standard]
pydantic
pydantic-settings
openai
chromadb
python-dotenv
pytest
sqlalchemy
psycopg[binary]
httpx

run:python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload

.env:all secret
test: pytest
architecture:
api endpoints:/health, /
database:


