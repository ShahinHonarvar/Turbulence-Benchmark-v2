def return_nth_smallest_ascii(s):
    substring = s[52:80]
    valid_chars = sorted(set(substring))
    if len(valid_chars) >= 7:
        return valid_chars[6]
    return None