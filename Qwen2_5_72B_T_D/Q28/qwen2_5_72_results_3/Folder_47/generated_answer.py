def return_nth_smallest_ascii(s):
    substring = s[3:53]
    valid_chars = sorted(set(substring))
    return valid_chars[7] if len(valid_chars) > 7 else None