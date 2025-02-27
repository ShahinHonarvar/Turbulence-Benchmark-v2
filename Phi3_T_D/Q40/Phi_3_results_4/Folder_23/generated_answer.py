def return_n_smallest_chars(string):
    return sorted([char for char in string if ord(char) <= 46])[:46]