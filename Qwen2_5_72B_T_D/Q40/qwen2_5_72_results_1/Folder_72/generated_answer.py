def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_37 = sorted_chars[:37]
    return sorted(smallest_37, key=ord, reverse=True)