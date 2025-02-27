def return_nth_smallest_ascii(s):
    substr = s[18:46]
    unique_chars = sorted(set(substr), key=ord)
    if len(unique_chars) >= 7:
        return unique_chars[6]
    return None