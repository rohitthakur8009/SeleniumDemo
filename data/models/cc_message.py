from dataclasses import (
    asdict,
    dataclass,
    field,
)


@dataclass
class CCMessage:
    name: str = 'Test User'
    email: str = 'test_email@yopmail.com'
    phone: str = '1234567890'
    message: str = 'This is a test message'
