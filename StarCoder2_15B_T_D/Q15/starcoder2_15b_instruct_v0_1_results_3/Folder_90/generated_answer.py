def sum_odd_ints_inclusive(numbers):
    sum_odd = 0
    for i, num in enumerate(numbers):
        if num % 2 != 0 and 262 <= i <= 746:
            sum_odd += num
    return sum_odd