def return_n_smallest_chars(string):
    sorted_string = sorted(string)
    smallest_chars = sorted_string[:34]
    return list(smallest_chars)