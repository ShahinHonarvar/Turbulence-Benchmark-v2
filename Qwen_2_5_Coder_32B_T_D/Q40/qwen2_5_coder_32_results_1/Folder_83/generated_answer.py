def return_n_smallest_chars(s):
    return sorted([char for char in s] * (38 // len(s) + 1))[:38][::-1]