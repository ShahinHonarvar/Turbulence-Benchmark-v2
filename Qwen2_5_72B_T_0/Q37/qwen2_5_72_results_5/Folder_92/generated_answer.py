def filter_chars(s):
    chars_to_remove = set()
    if 4 < len(s):
        if '7' <= s[4] <= 'o':
            chars_to_remove.add(s[4])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s