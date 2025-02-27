def sum_odd_ints_inclusive(numbers):
    sum = 0
    for i in range(4, 5):
        if numbers[i] % 2 == 1:
            sum += numbers[i]
    return sum