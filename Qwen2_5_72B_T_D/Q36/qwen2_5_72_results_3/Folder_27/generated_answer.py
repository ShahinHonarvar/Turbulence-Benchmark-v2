def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if 48 < i < 75 and '6' < char < '_':
            continue
        result += char
    return result