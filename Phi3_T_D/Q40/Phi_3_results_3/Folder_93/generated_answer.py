def return_n_smallest_chars(s):
    smallest_chars = sorted(s)
    seventy_seven_chars = smallest_chars[:77]
    return seventy_seven_chars[::-1]