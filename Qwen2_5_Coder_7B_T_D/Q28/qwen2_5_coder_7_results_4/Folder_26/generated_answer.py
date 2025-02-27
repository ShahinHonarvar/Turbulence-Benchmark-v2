def return_nth_smallest_ascii(s):
    filtered_chars = sorted([char for char in s[1:37] if char.isalpha()])
    if len(filtered_chars) < 15:
        return None
    return filtered_chars[14]