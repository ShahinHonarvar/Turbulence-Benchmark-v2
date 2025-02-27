def sum_even_ints_inclusive(int_list):
    sum_of_even = 0
    for i in range(29, 94):
        if int_list[i] % 2 == 0:
            sum_of_even += int_list[i]
    return sum_of_even