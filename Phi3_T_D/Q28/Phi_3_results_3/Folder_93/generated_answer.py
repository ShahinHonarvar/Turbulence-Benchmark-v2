def return_nth_smallest_ascii(s):
    target_chars = s[42:59 + 1]
    unique_chars = sorted(set(target_chars))
    return unique_chars[6]