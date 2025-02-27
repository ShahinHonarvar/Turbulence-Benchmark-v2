def filter_chars(s):
    modified = ''
    for i, char in enumerate(s):
        if 41 < i < 56 and 'Z' < char < 'c':
            modified += char
        elif i < 41 or i > 56:
            modified += char
    return modified