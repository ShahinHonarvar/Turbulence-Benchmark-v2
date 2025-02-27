def return_nth_smallest_ascii(s):
    filtered_chars = sorted([char for char in s[32:68] if char.isascii()])
    return filtered_chars[11] if len(filtered_chars) > 11 else None