def return_nth_smallest_ascii(s):
    filtered_chars = sorted([char for char in s[22:75] if char.isascii()])
    return filtered_chars[11] if len(filtered_chars) > 11 else None