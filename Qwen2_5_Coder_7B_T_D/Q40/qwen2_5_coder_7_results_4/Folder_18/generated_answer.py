def return_n_smallest_chars(s):
    return sorted(s[:52], key=lambda x: (x, -ord(x)), reverse=True)