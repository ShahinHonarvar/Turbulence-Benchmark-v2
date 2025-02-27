def sum_odd_ints_inclusive(numbers):
    if 6 < len(numbers):
        if numbers[6] % 2 != 0:
            return numbers[6]
    return 0