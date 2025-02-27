def filter_chars(s):
    for char in s[1:8]:
        if '3' < char < '^':
            s = s.replace(char, '')
    return s