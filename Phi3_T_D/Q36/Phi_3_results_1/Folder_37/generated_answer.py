def filter_chars(s):
    for char in s[44:59]:
        if '6' > char > '/':
            s = s.replace(char, '')
    return s