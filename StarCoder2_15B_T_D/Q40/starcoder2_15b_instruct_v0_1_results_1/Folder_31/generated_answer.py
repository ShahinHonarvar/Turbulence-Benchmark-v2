def return_n_smallest_chars(string):
    sorted_string = sorted(string)
    smallest_chars = sorted_string[:70]
    smallest_chars.reverse()
    return smallest_chars