def return_n_smallest_chars(s):
    chars = list(s)
    sorted_chars = sorted(chars)
    reversed_chars = sorted_chars[::-1]
    return reversed_chars[:47]