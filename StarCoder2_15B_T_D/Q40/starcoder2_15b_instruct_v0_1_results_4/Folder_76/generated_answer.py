def return_n_smallest_chars(string):
    chars = list(string)
    sorted_chars = sorted(chars)
    smallest_chars = sorted_chars[:3]
    return smallest_chars[::-1]