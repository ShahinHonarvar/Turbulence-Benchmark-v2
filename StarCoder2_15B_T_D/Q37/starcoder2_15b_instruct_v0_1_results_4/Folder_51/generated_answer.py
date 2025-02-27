def filter_chars(s):
    filtered = ''
    for char in s:
        if (char < 'H' or char > 'e') or (char < 'H' and char > 'e'):
            filtered += char
    return filtered