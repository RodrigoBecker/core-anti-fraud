import os

from app.interfaces.settings import Environments


class Setting:
    @classmethod
    def set_config(cls):
        return Environments(environment=os.environ["ENVIRONMENT"])
