def return_n_smallest_chars(string):
    unique_chars = sorted(set(string), key=ord)[:16]
    unique_chars.sort(reverse=True)
    return unique_chars