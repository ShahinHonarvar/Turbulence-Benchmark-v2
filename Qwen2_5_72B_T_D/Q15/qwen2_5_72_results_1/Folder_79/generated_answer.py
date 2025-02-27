def sum_odd_ints_inclusive(numbers):
    if 4 < len(numbers):
        if numbers[4] % 2 != 0:
            return numbers[4]
    return 0