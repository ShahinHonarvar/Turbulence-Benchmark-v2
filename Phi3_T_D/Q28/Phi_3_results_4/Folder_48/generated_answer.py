def return_nth_smallest_ascii(s):
    target_slice = s[37:60]
    unique_chars = sorted(set(target_slice))
    return unique_chars[5] if len(unique_chars) > 5 else None