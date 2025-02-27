def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[27:67]))
    if len(unique_chars) >= 15:
        return unique_chars[14]
    return None