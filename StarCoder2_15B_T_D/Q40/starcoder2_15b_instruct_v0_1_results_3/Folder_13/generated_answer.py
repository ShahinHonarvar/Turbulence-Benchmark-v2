def return_n_smallest_chars(string):
    sorted_string = sorted(string)
    sliced_string = sorted_string[:31]
    return list(sliced_string)