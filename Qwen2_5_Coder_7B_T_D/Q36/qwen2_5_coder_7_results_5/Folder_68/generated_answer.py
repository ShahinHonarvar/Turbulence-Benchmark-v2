def filter_chars(s):
    for char in s[1:9]:
        if '9' > char > '8' or 'm' > char > 'n':
            s = s.replace(char, '')
    return s