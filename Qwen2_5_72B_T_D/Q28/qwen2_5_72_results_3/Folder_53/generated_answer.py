def return_nth_smallest_ascii(s):
    subset = s[40:61]
    unique_chars = list(set(subset))
    unique_chars.sort(key=lambda c: ord(c))
    if len(unique_chars) < 19:
        return None
    return unique_chars[18]