def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[32:68] if char.isascii()]
    filtered_chars.sort()
    return filtered_chars[11]