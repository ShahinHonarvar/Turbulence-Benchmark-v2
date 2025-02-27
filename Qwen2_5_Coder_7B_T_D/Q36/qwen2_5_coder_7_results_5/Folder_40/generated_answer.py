def filter_chars(s):
    for char in s[1:8]:
        if '-' < char < 'L':
            s = s.replace(char, '')
    return s