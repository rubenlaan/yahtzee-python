import pytest

from yahtzee_python.score import score


@pytest.mark.parametrize("dices,expected", [
    ([1, 2, 3, 4, 5], 15),
    ([5, 5, 5, 5, 5], 25)
])
def test_score_should_return_sum_of_dices_given_chance(dices, expected):
    result = score(dices, "Chance")

    assert result == expected

def test_score_should_be_50_given_all_dices_are_the_same_and_scored_on_yahtzee():
    result = score([5, 5, 5, 5, 5], "Yahtzee")

    assert result == 50

def test_score_should_be_0_given_dices_are_different_and_scored_on_yahtzee():
    result = score([4, 5, 5, 5, 5], "Yahtzee")

    assert result == 0

