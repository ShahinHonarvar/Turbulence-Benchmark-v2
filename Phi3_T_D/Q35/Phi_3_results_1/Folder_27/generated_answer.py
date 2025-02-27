def remove_repeat_chars(s):
    start, end = (86, 89)
    chars_to_remove = set(s[start:end])
    for char in chars_to_remove:
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s