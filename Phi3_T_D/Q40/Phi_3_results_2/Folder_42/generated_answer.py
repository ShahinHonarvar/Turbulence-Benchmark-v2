def return_n_smallest_chars(input_string):
    sorted_list = sorted(input_string, reverse=True)[:59]
    return sorted_list