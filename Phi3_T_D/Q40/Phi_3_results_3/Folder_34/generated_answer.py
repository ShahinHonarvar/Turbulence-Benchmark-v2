def return_n_smallest_chars(string):
    smallest = sorted(string)[:9]
    return sorted(smallest, reverse=True)