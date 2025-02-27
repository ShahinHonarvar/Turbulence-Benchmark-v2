def sum_odd_ints_inclusive(numbers):
    sum_odd = 0
    for i, num in enumerate(numbers):
        if i >= 62 and i <= 78:
            if num % 2 != 0:
                sum_odd += num
    return sum_odd