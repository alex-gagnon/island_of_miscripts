import pytest

from src.classic_problems.fizzbuzz import fizzbuzz

@pytest.mark.parametrize('n', (
        51, 101, 151, 201
))
def test_fizzbuzz(n):
    response = fizzbuzz(n)
    for index, num in enumerate(range(1, n)):
        if index == 2:
            assert response[index] == "Fizz"
        elif index == 4:
            assert response[index] == "Buzz"
        elif index == 14:
            assert response[index] == "FizzBuzz"
        else:
            assert num in range(n)
