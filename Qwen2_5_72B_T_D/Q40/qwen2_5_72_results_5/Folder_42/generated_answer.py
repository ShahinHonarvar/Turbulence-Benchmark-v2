def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_59 = sorted_chars[:59]
    return sorted(smallest_59, reverse=True)