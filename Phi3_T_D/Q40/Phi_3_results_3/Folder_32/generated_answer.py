def return_n_smallest_chars(s):
    return sorted(list(filter(lambda x: ord(x) < 128, s)))[:8]