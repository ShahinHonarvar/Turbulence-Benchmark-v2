def return_n_smallest_chars(s):
    unique_chars = sorted(set(s))
    limited_list = unique_chars[-45:]
    limited_list.sort(reverse=True)
    return limited_list