def filter_chars(s):
    filtered = ''
    for char in s:
        if char < 'W' or char > '[':
            filtered += char
    return filtered