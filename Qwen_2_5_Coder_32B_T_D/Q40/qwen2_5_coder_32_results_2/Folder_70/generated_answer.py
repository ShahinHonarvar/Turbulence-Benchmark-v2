def return_n_smallest_chars(s):
    return sorted([min(s)], key=lambda x: ord(x))[-2::-1]