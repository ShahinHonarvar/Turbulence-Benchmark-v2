def filter_chars(s):
    for char in s[44:59]:
        if '1' <= char <= '5':
            s = s.replace(char, '')
    return s