from typing import Any
from fastapi import status, Response, Request, Header
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.infrastructure.logger import Logger


from app.interfaces.transaction_request_analyser import (
    TransactionRequestAnalyserInput,
    TransactionRequestAnalyserOutput,
)


router = InferringRouter()


@cbv(router)
class TransactionRequestAnalyserController:
    def __init__(self) -> None:
        self.__logger = Logger()

    @router.post(
        "/transaction-analyser",
        responses={
            status.HTTP_201_CREATED: {
                "model": "",
                "description": "",
            },
            status.HTTP_403_FORBIDDEN: {
                "model": "",
                "description": "",
            },
            status.HTTP_500_INTERNAL_SERVER_ERROR: {
                "model": "",
                "description": "",
            },
        },
    )
    async def execute_transaction_analyser(
        self, payload: TransactionRequestAnalyserInput
    ) -> Any:
        return TransactionRequestAnalyserOutput(
            ticket="000001",
            date="2023-10-22T08:30:00",
            message="Solicitacao enviada com sucesso !",
        ).dict()
