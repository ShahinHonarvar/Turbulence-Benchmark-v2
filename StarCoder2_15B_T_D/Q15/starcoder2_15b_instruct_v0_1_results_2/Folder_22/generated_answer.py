def sum_odd_ints_inclusive(numbers):
    sum = 0
    for i in range(40, 42):
        if numbers[i] % 2 == 1:
            sum += numbers[i]
    return sum