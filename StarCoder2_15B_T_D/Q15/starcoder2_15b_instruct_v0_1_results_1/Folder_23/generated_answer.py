def sum_odd_ints_inclusive(numbers):
    sum_of_odd_ints = 0
    for i in range(52, 72):
        if numbers[i] % 2 != 0:
            sum_of_odd_ints += numbers[i]
    return sum_of_odd_ints