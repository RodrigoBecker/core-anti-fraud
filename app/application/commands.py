from app.application.use_cases.check_name_analyser import CheckNameAnalyser
from app.application.use_cases.check_address_analyser import CheckAddressAnalyser
from transitions import Machine

from app.infrastructure.logger import Logger


class AntiFrudEngine:
    states = [
        "transaction_received",
        "start_verifications",
        "checked_name",
        "checked_address",
    ]

    def __init__(self, transaction_data) -> None:
        self.__rule_address = CheckAddressAnalyser()
        self.__rule_name = CheckNameAnalyser()
        self.__logger = Logger()
        self.__data = transaction_data

        # Initialize the state machine
        self.machine = Machine(
            model=self, states=AntiFrudEngine.states, initial="transaction_received"
        )

        # Add transitions.
        self.machine.add_transition(
            trigger="start",
            source="transaction_received",
            dest="start_verifications",
        )

        self.machine.add_transition(
            trigger="run_check_name",
            source="start_verifications",
            dest="checked_name",
            before="run_check_name",
        )
        self.machine.add_transition(
            trigger="run_check_address",
            source="checked_name",
            dest="checked_address",
            before="run_check_address",
        )

    def run_check_name(self):
        self.__logger.attribute.info("run check name")
        self.__rule_name.validate_name(data=self.__data, ticket="0001")
        return

    def run_check_address(self):
        self.__logger.attribute.info("run check address")
        self.__rule_address.validate_address(data=self.__data, ticket="0001")
