def return_nth_smallest_ascii(s):
    sliced_chars = s[34:86]
    sorted_chars = sorted(set(sliced_chars))
    if len(sorted_chars) >= 20:
        return sorted_chars[19]
    return None