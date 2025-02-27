def sum_even_ints_inclusive(input_list):
    sum_even_ints = 0
    for i in range(56, 67):
        if input_list[i] % 2 == 0:
            sum_even_ints += input_list[i]
    return sum_even_ints