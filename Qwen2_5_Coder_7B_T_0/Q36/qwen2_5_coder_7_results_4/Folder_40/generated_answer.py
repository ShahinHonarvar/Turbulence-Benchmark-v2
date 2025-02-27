def filter_chars(s):
    for char in s[1:7]:
        if '-' < char < 'L':
            s = s.replace(char, '')
    return s