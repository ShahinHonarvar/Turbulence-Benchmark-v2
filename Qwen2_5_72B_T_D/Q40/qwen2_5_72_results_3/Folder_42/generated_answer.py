def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_59 = sorted_chars[:59]
    return sorted(smallest_59, key=ord, reverse=True)