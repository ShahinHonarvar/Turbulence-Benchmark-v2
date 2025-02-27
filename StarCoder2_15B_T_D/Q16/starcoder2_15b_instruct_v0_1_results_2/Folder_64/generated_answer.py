def sum_even_ints_inclusive(lst):
    sum_even = 0
    for i, num in enumerate(lst):
        if i > 4:
            break
        if num % 2 == 0:
            sum_even += num
    if sum_even == 0:
        return 0
    return sum_even