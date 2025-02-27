def filter_chars(s):
    chars_to_remove = set()
    for i in range(219, 403):
        if '7' > s[i] > '*':
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s