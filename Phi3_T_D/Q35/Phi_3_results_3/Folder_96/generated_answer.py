def remove_repeat_chars(s):
    start, end = (60, 200)
    chars_to_remove = [s[i] for i in range(start, end) if s.count(s[i], start, end) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s