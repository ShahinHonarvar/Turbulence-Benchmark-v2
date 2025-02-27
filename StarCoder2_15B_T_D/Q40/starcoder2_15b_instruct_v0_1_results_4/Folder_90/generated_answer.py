def return_n_smallest_chars(input_string):
    input_list = list(input_string)
    input_list.sort()
    return input_list[-24:]