def return_n_smallest_chars(s):
    return sorted(s[:88], key=lambda x: -ord(x))