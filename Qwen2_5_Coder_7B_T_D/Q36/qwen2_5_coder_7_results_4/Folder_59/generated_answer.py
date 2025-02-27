def filter_chars(s):
    chars_to_remove = set()
    for i in range(3, 8):
        char = s[i]
        if '?' < char < 'k':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s