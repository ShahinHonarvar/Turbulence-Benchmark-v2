def sum_even_ints_inclusive(int_list):
    sum_even = 0
    for i, num in enumerate(int_list):
        if i >= 25 and i <= 87 and (num % 2 == 0):
            sum_even += num
    return sum_even