def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[25:89]))
    return unique_chars[10] if len(unique_chars) > 10 else None