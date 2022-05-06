from dataclasses import (
    asdict,
    dataclass,
    field,
)


@dataclass
class Address:
    address_street: str = 'Abc Lane'
    city: str = 'Dallas'
    state: str = 'Texas'
    zipcode: str = '12345'


@dataclass
class Account:
    username: str = ''
    password: str = ''
    first_name: str = 'Test'
    last_name: str = 'User'
    ssn: str = '000-00-0000'
    phone_no: str = '1234567890'
    address: Address = Address()


