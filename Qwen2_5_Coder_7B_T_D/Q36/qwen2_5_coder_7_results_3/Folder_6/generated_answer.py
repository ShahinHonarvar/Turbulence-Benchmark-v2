def filter_chars(s):
    result = ''
    for i, char in enumerate(s):
        if not 31 < i < 70 or not 'B' < char < 'v':
            result += char
    return result