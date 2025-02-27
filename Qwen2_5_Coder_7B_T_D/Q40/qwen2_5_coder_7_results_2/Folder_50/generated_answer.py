def return_n_smallest_chars(s):
    return sorted(s[:16], key=lambda x: -ord(x))