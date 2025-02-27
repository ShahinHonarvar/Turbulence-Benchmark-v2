def return_nth_smallest_ascii(s):
    s_slice = s[34:82]
    unique_chars = sorted(set(s_slice), key=ord)
    if len(unique_chars) < 12:
        return None
    return unique_chars[11]