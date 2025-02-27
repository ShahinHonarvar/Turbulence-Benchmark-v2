def remove_repeat_chars(s):
    char_range = s[55:84]
    seen_chars = set()
    filtered_chars = [char for char in char_range if not (char in seen_chars or seen_chars.add(char))]
    return s[:55] + ''.join(filtered_chars) + s[84:]