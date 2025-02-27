def return_nth_smallest_ascii(s):
    unique_chars = sorted(dict.fromkeys(s[29:48]))
    if len(unique_chars) < 7:
        return None
    return unique_chars[6]