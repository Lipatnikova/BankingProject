from dataclasses import dataclass


@dataclass
class Customer:
    first_name: str = None
    last_name: str = None
    post_code: str = None


class DataAddCustomer:
    MSG_SUCCESS = "Customer added successfully with customer id"
