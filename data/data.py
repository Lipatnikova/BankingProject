from dataclasses import dataclass


@dataclass
class Customer:
    last_name: str = None


class DataAddCustomer:
    MSG_SUCCESS = "Customer added successfully with customer id"
