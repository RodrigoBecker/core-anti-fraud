import json
import sys
from loguru import logger


def serialize(record):
    subset = {
        "timestamp": record["time"].__str__(),
        "message": record["message"],
        "level": record["level"].name,
        "origin": record["name"],
        "line": record["line"],
    }
    return json.dumps(subset)


def patching(record):
    record["extra"]["serialized"] = serialize(record)


class Logger:
    def __init__(self) -> None:
        super().__init__()
        self.__logger = logger
        self.__logger.remove(0)

    @property
    def attribute(self):
        logger = self.__logger.patch(patching)
        logger.add(sys.stderr, format="{extra[serialized]}")
        return logger
