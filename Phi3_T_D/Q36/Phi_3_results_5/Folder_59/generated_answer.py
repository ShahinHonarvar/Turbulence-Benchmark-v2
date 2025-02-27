def filter_chars(s):
    for i in range(3, 8):
        char = s[i]
        if '?' < char < 'k':
            s = s.replace(char, '')
    return s