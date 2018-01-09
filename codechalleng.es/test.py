from numbers import sum_numbers


def test_sum_numbers():
    assert sum_numbers(range(1, 11)) == 55
    assert sum_numbers() == 5050

test_sum_numbers()
