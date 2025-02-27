def sum_even_ints_inclusive(lst):
    sum_even_ints = 0
    for idx, num in enumerate(lst):
        if idx >= 91 and idx <= 99 and (num % 2 == 0):
            sum_even_ints += num
    return sum_even_ints