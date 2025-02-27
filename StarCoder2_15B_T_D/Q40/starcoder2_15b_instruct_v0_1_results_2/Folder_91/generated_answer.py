def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    reversed_chars = sorted_chars[:6][::-1]
    result_list = list(reversed_chars)
    return result_list