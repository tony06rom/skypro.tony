import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "input_user, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("8349567456546756", "8349 56** **** 6756"),
        ("quit", "До свидания!"),
    ],
)
def test_get_mask_card_number(input_user, expected):
    assert get_mask_card_number(input_user) == expected


@pytest.mark.parametrize(
    "input_user, expected",
    [("46785685687932455544", "**5544"), ("73654108430135874305", "**4305"), ("quit", "До свидания!")],
)
def test_get_mask_account(input_user, expected):
    assert get_mask_account(input_user) == expected
