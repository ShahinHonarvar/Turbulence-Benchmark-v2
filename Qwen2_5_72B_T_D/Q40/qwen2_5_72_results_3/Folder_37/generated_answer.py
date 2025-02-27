def return_n_smallest_chars(s):
    return sorted([char for char in s[:26]], reverse=True)[:26]