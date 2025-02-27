def sum_even_ints_inclusive(ints):
    sum_even = 0
    for i, num in enumerate(ints):
        if i >= 62 and i <= 92 and (num % 2 == 0):
            sum_even += num
    return sum_even