def return_nth_smallest_ascii(s):
    subset = s[18:67]
    unique_chars = sorted(set(subset))
    return unique_chars[18] if len(unique_chars) > 18 else None