def return_n_smallest_chars(s):
    return sorted(s[:59], key=lambda x: ord(x), reverse=True)