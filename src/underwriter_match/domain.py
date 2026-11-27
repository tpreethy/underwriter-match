"""Core domain types for underwriter match."""

from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum


class LoanType(StrEnum):
    """Kinds of loans the lender offers.Values are stored in the database and audit trail."""

    MORTGAGE = "mortgage"
    AUTO = "auto"
    PERSONAL = "personal"
    SMALL_BUSINESS = "small_business"


@dataclass(frozen=True, slots=True, kw_only=True)
class Underwriter:
    """A loan underwriter who can be assigned loan applications.
    A region of None means the underwriter covers all regions.

    Holds only the information needed to assign a loan application to an
    underwriter, with no personal information about the underwriter.
    """

    id: int
    loan_types: frozenset[LoanType]
    max_loan_amount: Decimal
    active_cases: int
    max_cases: int
    region: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class LoanApplication:
    """A loan application that needs to be assigned to an underwriter.

    Includes only the information needed to assign the application to an underwriter,
    with no personal information about the applicant.
    """

    id: str
    loan_type: LoanType
    amount: Decimal
    region: str
