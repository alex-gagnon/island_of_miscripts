import pytest

from . import classic_problems


@pytest.mark.parametrize('n', (
        51, 101, 151, 201
))
def test_fizzbuzz(n):
    response = classic_problems.fizzbuzz(n)
    for index, num in enumerate(range(1, n)):
        if index == 2:
            assert response[index] == "Fizz"
        elif index == 4:
            assert response[index] == "Buzz"
        elif index == 14:
            assert response[index] == "FizzBuzz"
        else:
            assert num in range(n)
