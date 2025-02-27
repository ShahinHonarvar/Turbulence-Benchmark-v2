def sum_even_ints_inclusive(int_list):
    total = 0
    for i, num in enumerate(int_list):
        if i >= 40 and i <= 41 and (num % 2 == 0):
            total += num
    return total