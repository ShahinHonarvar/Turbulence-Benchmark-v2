def return_n_smallest_chars(s):
    smallest = sorted(list(s), key=ord)[:2]
    return sorted(smallest, reverse=True)