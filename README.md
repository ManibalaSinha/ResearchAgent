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

pip install fastapi uvicorn
pip install -r requirements.txt
uvicorn app.main:app --reload

test: pip install pytest pytest-asyncio httpx
pytest -v

architecture:
api endpoints:/health, /
database:


