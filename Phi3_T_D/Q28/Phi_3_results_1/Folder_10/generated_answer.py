def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[38:83]))
    return unique_chars[19] if len(unique_chars) >= 20 else None