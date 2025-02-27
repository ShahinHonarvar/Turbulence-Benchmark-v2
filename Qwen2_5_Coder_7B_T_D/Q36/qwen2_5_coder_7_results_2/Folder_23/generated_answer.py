def filter_chars(s):
    substring = s[21:25]
    for char in substring:
        if char > '5' and char < '}':
            s = s.replace(char, '')
    return s