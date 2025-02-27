def remove_repeat_chars(s):
    unique_chars = {c for c in s[32:99] if s.count(c, 32, 99) > 1}
    for char in unique_chars:
        s = s.replace(char, '')
    return s