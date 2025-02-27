def sum_even_ints_inclusive(input_list):
    if len(input_list) < 69:
        raise ValueError('The input list is too short.')
    output_sum = 0
    for i in range(13, 69):
        if input_list[i] % 2 == 0:
            output_sum += input_list[i]
    return output_sum