def sum_odd_ints_inclusive(numbers):
    sum_ = 0
    for i in range(23, 24):
        if numbers[i] % 2 != 0:
            sum_ += numbers[i]
    return sum_