def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[32:68] if char.isascii()]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[11]