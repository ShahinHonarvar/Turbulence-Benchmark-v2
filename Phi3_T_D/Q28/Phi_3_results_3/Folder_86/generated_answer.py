def return_nth_smallest_ascii(s):
    subset = s[44:70]
    unique_chars = sorted(set(subset), key=lambda x: ord(x))
    if len(unique_chars) < 15:
        return None
    return unique_chars[14]