def filter_chars(s):
    chars_to_remove = set((ch for ch in s[503:754] if '9' <= ch <= 'w'))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s