def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=ord)
    smallest_77 = sorted_s[:77]
    return sorted(smallest_77, key=ord, reverse=True)