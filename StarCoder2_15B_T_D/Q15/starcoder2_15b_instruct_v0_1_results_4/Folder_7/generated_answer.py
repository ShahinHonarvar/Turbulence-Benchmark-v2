def sum_odd_ints_inclusive(numbers):
    total = 0
    for i in range(661, 925):
        if numbers[i] % 2 == 1:
            total += numbers[i]
    return total