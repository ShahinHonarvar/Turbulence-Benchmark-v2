def sum_even_ints_inclusive(my_list):
    sum_even = 0
    for i in range(8, 10):
        if my_list[i] % 2 == 0:
            sum_even += my_list[i]
    return sum_even