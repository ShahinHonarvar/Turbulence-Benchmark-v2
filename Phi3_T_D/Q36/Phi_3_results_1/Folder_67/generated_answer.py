def filter_chars(s):
    for i in range(18, 32):
        char = s[i]
        if 'H' < char < '|':
            s = s.replace(char, '')
    return s