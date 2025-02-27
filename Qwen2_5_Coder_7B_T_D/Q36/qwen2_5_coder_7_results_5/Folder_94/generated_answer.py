def filter_chars(s):
    for char in s[15:85]:
        if char > 'I' and char < 'M':
            s = s.replace(char, '')
    return s