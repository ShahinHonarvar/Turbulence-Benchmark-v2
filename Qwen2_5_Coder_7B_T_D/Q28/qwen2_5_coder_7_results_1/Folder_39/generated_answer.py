def return_nth_smallest_ascii(s):
    filtered_chars = sorted([char for char in s[1:67] if char.isascii()])
    return filtered_chars[7] if len(filtered_chars) >= 8 else None