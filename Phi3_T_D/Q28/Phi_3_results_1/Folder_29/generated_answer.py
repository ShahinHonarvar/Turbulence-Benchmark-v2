def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[5:11]))
    if len(unique_chars) < 6:
        return None
    return unique_chars[5]