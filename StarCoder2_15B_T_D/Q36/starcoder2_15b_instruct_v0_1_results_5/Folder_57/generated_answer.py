def filter_chars(string):
    filtered = ''
    for i, char in enumerate(string):
        if not (70 < i < 74 and 'A' < char < 'U'):
            filtered += char
    return filtered