def return_nth_smallest_ascii(s):
    target_chars = s[40:61]
    unique_chars = sorted(set(target_chars))
    if len(unique_chars) < 19:
        return None
    return unique_chars[18]