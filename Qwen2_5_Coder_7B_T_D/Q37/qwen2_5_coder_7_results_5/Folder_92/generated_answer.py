def filter_chars(s):
    chars_to_remove = set('78901234567890')
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s[4:5]