def return_n_smallest_chars(s):
    return sorted(s[:3], key=lambda x: ord(x), reverse=True)