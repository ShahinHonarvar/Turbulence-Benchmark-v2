def return_n_smallest_chars(string):
    sorted_string = sorted(string)
    return sorted_string[:64][::-1]