from app.infrastructure.logger import Logger
from app.interfaces.transaction_request_analyser import TransactionRequestAnalyserInput


class CheckNameAnalyser:
    def __init__(self) -> None:
        self.__logger = Logger()

    def validate_name(self, data: TransactionRequestAnalyserInput, ticket: str) -> bool:
        self.__logger.attribute.info(f"Start verification name - ticket {ticket}")

        purchaser_name = data.billingData.client.name
        cardhold_name = data.paymentData.card.cardholderName

        if purchaser_name in cardhold_name:
            self.__logger.attribute.success(
                f"checked verification purchaser name is same cardholder name - ticket {ticket}"
            )
            return True

        self.__logger.attribute.info(
            f"checked purchaser name is not same cardholder name - ticket {ticket}"
        )
        return False
