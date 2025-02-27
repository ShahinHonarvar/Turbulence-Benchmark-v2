def sum_odd_ints_inclusive(numbers):
    return sum((numbers[i] for i in range(6) if numbers[i] % 2 != 0))