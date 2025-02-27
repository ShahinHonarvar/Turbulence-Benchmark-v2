def filter_chars(s):
    start, end = (43, 83)
    chars_to_remove = []
    for i in range(start, end):
        if ':' < s[i] < 'Q':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s