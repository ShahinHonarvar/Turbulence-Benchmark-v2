def return_nth_smallest_ascii(s):
    filtered_chars = sorted([char for char in s[33:86] if char.isascii()])
    return filtered_chars[12]