def return_nth_smallest_ascii(s):
    substring = s[14:36]
    unique_chars = sorted(set(substring))
    if len(unique_chars) < 11:
        return None
    return unique_chars[10]