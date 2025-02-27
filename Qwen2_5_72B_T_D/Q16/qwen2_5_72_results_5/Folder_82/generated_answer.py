def sum_even_ints_inclusive(numbers):
    if 29 < len(numbers):
        if numbers[29] % 2 == 0:
            return numbers[29]
        else:
            return 0
    else:
        return 0