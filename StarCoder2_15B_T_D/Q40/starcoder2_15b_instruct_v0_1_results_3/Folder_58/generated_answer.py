def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    sliced_chars = sorted_chars[:49]
    reversed_chars = reversed(sliced_chars)
    return list(reversed_chars)