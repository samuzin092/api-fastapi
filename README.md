# To create a virtual environment in Python (Linux Operating System)
$ python3 -m venv myenv
# To enable the Python virtual environment (Linux Operating System)

$ source myenv/bin/activate

pip install -r requirements.txt

# iniciar servidor
uvicorn server:app --reload
uvicorn server:app --reload --reload-dir=src

uvicorn src.server:app --reload

# alambican migrations
alembic init alembic

alembic revision --autogenerate -m "Initial"

alembic upgrade head