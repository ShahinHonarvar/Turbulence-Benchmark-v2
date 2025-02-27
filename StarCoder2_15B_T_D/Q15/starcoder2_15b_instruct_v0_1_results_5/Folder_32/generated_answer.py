def sum_odd_ints_inclusive(numbers):
    sum_odd = 0
    for i in range(21, 98):
        if numbers[i] % 2 == 1:
            sum_odd += numbers[i]
    return sum_odd