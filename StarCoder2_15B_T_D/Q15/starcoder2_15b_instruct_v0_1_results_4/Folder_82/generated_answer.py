def sum_odd_ints_inclusive(input_list):
    sum_of_odd_ints = 0
    for i in range(20, 201):
        if input_list[i] % 2 != 0:
            sum_of_odd_ints += input_list[i]
    return sum_of_odd_ints