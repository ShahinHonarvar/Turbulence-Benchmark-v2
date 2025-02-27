def sum_odd_ints_inclusive(numbers):
    sum_odd = 0
    for i in range(91, 100):
        if numbers[i] % 2 != 0:
            sum_odd += numbers[i]
    return sum_odd