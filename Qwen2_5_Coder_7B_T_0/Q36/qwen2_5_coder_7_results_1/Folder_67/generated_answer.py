def filter_chars(s):
    for char in s[18:31]:
        if 'H' < char < '|':
            s = s.replace(char, '')
    return s