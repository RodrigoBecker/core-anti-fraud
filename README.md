# Core Anti Fraud - POC 

## Project Struct 

```
├── .git
├── .venv
├── app
│   ├── adapters
│   │   ├── **/*.py
│   ├── application
│   │   ├── use_cases
│   │       ├── **/*.py
│   ├── domain 
│   │   ├── **/*.py
│   ├── infrastructure
│   │   ├── **/*.py
│   │   ├── db_service
│   │       ├── **/*.py
│   ├── interfaces
│   │   ├── **/*.py
│   ├── repositories
│   │   ├── **/*.py
│   ├── routes
│   │   ├── **/*.py
│   ├── services
│   │   ├── **/*.py
│   ├── utils
│   │   ├── **/*.py
├── tests
│   ├── __init__.py
│   ├── **/*.py
├── api.py
├── main.py
├── .env
├── .env_template
├── .gitignore
├── .flake8
├── .pre-commit-config.yaml
├── pyproject.toml
├── poetry.lock
└── README.md
```


## Dependencies:

* mangun [https://mangum.io]
* Pydantic [https://docs.pydantic.dev/latest]
* FastApi [https://fastapi.tiangolo.com]
* FastApi-Util [https://fastapi-utils.davidmontague.xyz]
* Transitions [https://github.com/pytransitions/transitions]
* Uvicorn [https://www.uvicorn.org]
* Httpx [https://www.python-httpx.org]
* Loguru [https://github.com/Delgan/loguru]
---

## Dependencies Developer:

* Black [https://github.com/psf/black]
* Pytest [https://docs.pytest.org/en/7.4.x]
* Pre-commit [https://pre-commit.com]
* Safety [https://pypi.org/project/safety] 
* Mypy [https://mypy-lang.org]

