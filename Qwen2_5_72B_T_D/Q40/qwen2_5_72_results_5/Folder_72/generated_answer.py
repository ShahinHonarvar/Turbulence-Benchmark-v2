def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_37 = sorted_chars[:37]
    return sorted(smallest_37, reverse=True)