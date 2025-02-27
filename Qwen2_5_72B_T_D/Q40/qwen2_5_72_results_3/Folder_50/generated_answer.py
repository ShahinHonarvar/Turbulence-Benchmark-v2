def return_n_smallest_chars(s):
    smallest = sorted(s)[:16]
    return sorted(smallest, reverse=True)