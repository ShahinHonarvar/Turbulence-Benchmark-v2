def return_nth_smallest_ascii(s):
    substring = s[28:68]
    valid_chars = sorted(set(substring))
    if len(valid_chars) < 15:
        return None
    return valid_chars[14]