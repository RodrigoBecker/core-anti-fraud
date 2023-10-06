from typing import Any
from fastapi import status, Response
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.infrastructure.logger import Logger


from app.interfaces.commons import (
    HeathCheckOutputBadGateway,
    HeathCheckOutputInternalError,
    HeathCheckOutputSuccess,
    HeathCheckOutputTimeOut,
)


router = InferringRouter()


@cbv(router)
class HealthCheckController:
    def __init__(self) -> None:
        self.__logger = Logger()

    @router.get(
        "/health",
        responses={
            status.HTTP_200_OK: {
                "model": HeathCheckOutputSuccess,
                "description": HeathCheckOutputSuccess().message,
            },
            status.HTTP_500_INTERNAL_SERVER_ERROR: {
                "model": HeathCheckOutputInternalError,
                "description": HeathCheckOutputInternalError().message,
            },
            status.HTTP_502_BAD_GATEWAY: {
                "model": HeathCheckOutputBadGateway,
                "description": HeathCheckOutputBadGateway().message,
            },
            status.HTTP_504_GATEWAY_TIMEOUT: {
                "model": HeathCheckOutputTimeOut,
                "description": HeathCheckOutputTimeOut().message,
            },
        },
    )
    async def get_health(self, resp: Response) -> Any:
        self.__logger.attribute.info("sdsdsd")

        if resp == status.HTTP_500_INTERNAL_SERVER_ERROR:
            return HeathCheckOutputInternalError().dict()

        if resp == status.HTTP_502_BAD_GATEWAY:
            return HeathCheckOutputBadGateway().dict()

        if resp == status.HTTP_504_GATEWAY_TIMEOUT:
            return HeathCheckOutputTimeOut().dict()

        return HeathCheckOutputSuccess().dict()
