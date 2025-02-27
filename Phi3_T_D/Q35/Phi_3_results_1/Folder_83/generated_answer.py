def remove_repeat_chars(s):
    chars_to_remove = [c for i, c in enumerate(s[100:200]) if s[100:200].count(c) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s