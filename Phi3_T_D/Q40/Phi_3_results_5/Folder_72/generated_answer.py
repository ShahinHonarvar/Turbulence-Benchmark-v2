def return_n_smallest_chars(s):
    smallest_chars = sorted(s, reverse=True)[:37]
    return smallest_chars