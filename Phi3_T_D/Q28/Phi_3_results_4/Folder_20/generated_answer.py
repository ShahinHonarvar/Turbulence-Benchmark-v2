def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[25:65]))
    return unique_chars[5] if len(unique_chars) > 5 else None