from enum import Enum


class DocumentType(str, Enum):
    UNKNOWN = "unknown"
    PAYMENT_REQUEST = "payment_request"
    PAYMENT_REMINDER = "payment_reminder"
    MAHNUNG = "mahnung"
    FESTSETZUNGSBESCHEID = "festsetzungsbescheid"
    REGISTRATION = "registration"