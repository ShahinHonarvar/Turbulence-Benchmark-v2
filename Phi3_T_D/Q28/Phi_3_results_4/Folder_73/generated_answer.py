def return_nth_smallest_ascii(s):
    valid_chars = sorted(set(s[0:70]))
    return valid_chars[9] if len(valid_chars) >= 10 else None