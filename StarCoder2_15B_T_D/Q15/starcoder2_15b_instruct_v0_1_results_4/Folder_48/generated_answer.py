def sum_odd_ints_inclusive(numbers):
    sum = 0
    for i in range(533, 606):
        if numbers[i] % 2 != 0:
            sum += numbers[i]
    return sum