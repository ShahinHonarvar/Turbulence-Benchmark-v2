def return_n_smallest_chars(input_string):
    input_list = list(input_string)
    smallest_chars = sorted(input_list)[:29]
    return smallest_chars