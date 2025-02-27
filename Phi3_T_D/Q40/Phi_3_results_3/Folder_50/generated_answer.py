def return_n_smallest_chars(s):
    selected_chars = sorted(s, key=ord)[0:16]
    selected_chars.sort(key=ord, reverse=True)
    return selected_chars