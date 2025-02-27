def return_n_smallest_chars(s):
    return sorted(sorted(s), key=lambda x: (x, -ord(x)), reverse=True)[:33]