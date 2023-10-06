from app.infrastructure.logger import Logger
from app.interfaces.transaction_request_analyser import TransactionRequestAnalyserInput


class CheckAddressAnalyser:
    def __init__(self) -> None:
        self.__logger = Logger()

    def validate_address(
        self, data: TransactionRequestAnalyserInput, ticket: str
    ) -> bool:
        self.__logger.attribute.info(f"Start verification address - ticket {ticket}")

        delivery_address = data.shippingData.address
        purchaser_address = data.billingData.address

        if (
            delivery_address.street == purchaser_address.street
            and delivery_address.state == purchaser_address.state
            and delivery_address.city == purchaser_address.city
            and delivery_address.contry == purchaser_address.contry
            and delivery_address.number == purchaser_address.number
            and delivery_address.district == purchaser_address.district
            and delivery_address.zipcode == purchaser_address.zipcode
            and delivery_address.neighborhood == purchaser_address.neighborhood
        ):
            self.__logger.attribute.success(
                f"checked verification purchaser address is same delivery_address - ticket {ticket}"
            )
            return True
        self.__logger.attribute.success(
            f"checked verification purchaser address is not same delivery_address - ticket {ticket}"
        )
        return False
