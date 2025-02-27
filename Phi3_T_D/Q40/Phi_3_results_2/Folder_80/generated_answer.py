def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)[:35]
    return sorted_chars