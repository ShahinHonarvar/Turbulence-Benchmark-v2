def filter_chars(s):
    j = 63
    while j < 89:
        char = s[j]
        if '*' < char < 'w':
            s = s.replace(char, '')
        j += 1
    return s