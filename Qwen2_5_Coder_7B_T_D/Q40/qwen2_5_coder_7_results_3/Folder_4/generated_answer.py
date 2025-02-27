def return_n_smallest_chars(s):
    return sorted(s[:90], key=lambda x: (ord(x), -ord(x)), reverse=True)