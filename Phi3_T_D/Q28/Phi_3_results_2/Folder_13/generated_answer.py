def return_nth_smallest_ascii(s):
    valid_chars = sorted(set(s[47:81]))
    if len(valid_chars) >= 4:
        return valid_chars[3]
    return None