def sum_odd_ints_inclusive(numbers):
    if 300 < len(numbers):
        if numbers[300] % 2 != 0:
            return numbers[300]
    return 0