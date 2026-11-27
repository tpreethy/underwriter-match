from decimal import Decimal

from underwriter_match.domain import LoanType, Underwriter, has_capacity


def make_underwriter(*, active_cases: int, max_cases: int = 10) -> Underwriter:
    """Build a valid Underwriter, letting each test set only what it cares about."""
    return Underwriter(
        id=1,
        loan_types=frozenset({LoanType.MORTGAGE}),
        max_loan_amount=Decimal("500000.00"),
        active_cases=active_cases,
        max_cases=max_cases,
    )


def test_has_capacity_when_below_max() -> None:
    underwriter = make_underwriter(active_cases=9, max_cases=10)
    assert has_capacity(underwriter) is True


def test_no_capacity_when_at_max() -> None:
    underwriter = make_underwriter(active_cases=10, max_cases=10)
    assert has_capacity(underwriter) is False
