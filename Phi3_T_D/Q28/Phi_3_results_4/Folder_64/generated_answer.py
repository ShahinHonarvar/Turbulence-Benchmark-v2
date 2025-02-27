def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[:7]))
    char_count = len(unique_chars)
    if char_count < 7:
        return None
    return unique_chars[6]