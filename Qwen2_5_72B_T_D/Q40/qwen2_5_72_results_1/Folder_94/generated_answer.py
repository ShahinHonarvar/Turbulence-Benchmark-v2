def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_87 = sorted_chars[:87]
    return sorted(smallest_87, key=ord, reverse=True)