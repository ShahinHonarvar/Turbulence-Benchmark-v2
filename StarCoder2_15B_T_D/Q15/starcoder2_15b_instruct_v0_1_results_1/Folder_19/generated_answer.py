def sum_odd_ints_inclusive(numbers):
    sum_odd = 0
    for i, num in enumerate(numbers):
        if i >= 3 and i <= 5 and (num % 2 != 0):
            sum_odd += num
    return sum_odd