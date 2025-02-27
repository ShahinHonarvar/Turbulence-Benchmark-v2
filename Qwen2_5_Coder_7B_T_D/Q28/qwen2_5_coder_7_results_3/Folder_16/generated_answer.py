def return_nth_smallest_ascii(s):
    filtered_chars = sorted([char for char in s[18:46] if char.isalpha()])
    return filtered_chars[6]