def return_nth_smallest_ascii(s):
    sliced_chars = s[50:77]
    sorted_chars = sorted(set(sliced_chars))
    return sorted_chars[10]