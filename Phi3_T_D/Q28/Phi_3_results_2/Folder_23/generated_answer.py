def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[28:48]))
    return unique_chars[6] if len(unique_chars) >= 7 else None