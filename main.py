import uvicorn

from api import create_app

app = create_app()

if __name__ == "__main__":
    params = {"host": "0.0.0.0", "port": 8000}
    uvicorn.run(app, **params)
