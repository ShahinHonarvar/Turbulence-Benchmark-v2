def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[52:79 + 1]))
    if len(unique_chars) >= 7:
        return unique_chars[6]
    return None