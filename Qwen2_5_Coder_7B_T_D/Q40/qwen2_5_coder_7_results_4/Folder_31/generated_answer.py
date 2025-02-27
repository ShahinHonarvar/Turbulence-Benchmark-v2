def return_n_smallest_chars(s):
    n = min(70, len(s))
    return sorted(s[:n], key=lambda x: (ord(x), -s.index(x)), reverse=True)