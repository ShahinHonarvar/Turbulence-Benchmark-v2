def return_n_smallest_chars(s):
    return sorted([char for char in s], key=ord)[::-1]