def return_nth_smallest_ascii(s):
    filtered_chars = sorted([s[i] for i in range(18, 46) if s[i].isascii()])
    return filtered_chars[6]