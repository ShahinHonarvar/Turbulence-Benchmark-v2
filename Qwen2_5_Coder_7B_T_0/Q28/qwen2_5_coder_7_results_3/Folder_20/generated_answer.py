def return_nth_smallest_ascii(s):
    filtered_chars = sorted([char for char in s[25:65] if char.isascii()])
    return filtered_chars[5] if len(filtered_chars) >= 6 else None