"""Core domain types for underwriter match."""

from enum import StrEnum


class LoanType(StrEnum):
    """Kinds of loans the lender offers.Values are stored in the database and audit trail."""

    MORTGAGE = "mortgage"
    AUTO = "auto"
    PERSONAL = "personal"
    SMALL_BUSINESS = "small_business"
