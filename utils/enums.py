from enum import Enum


class ItemType(str, Enum):
    basic = "basic"
    premium = "premium"


class ErrorMessageCodes(str, Enum):
    NOT_FOUND = "NOT_FOUND"
    BAD_REQUEST = "BAD_REQUEST"
    ALREADY_EXISTS = "ALREADY_EXISTS"
