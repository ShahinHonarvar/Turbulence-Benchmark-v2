def remove_repeat_chars(s):
    first_half = s[:8:2]
    char_to_remove = next((char for char in first_half if first_half.count(char) > 1), None)
    if char_to_remove:
        s = s.replace(char_to_remove, '', first_half.count(char_to_remove))
    return s