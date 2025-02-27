def return_nth_smallest_ascii(s):
    if len(s) < 46:
        return None
    substring = s[:46]
    unique_chars = sorted(set(substring))
    if len(unique_chars) < 10:
        return None
    return unique_chars[9]