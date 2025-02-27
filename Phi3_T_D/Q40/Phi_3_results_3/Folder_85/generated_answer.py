def return_n_smallest_chars(s):
    s = sorted(s)
    s = s[len(s) - 85:]
    return s[::-1]