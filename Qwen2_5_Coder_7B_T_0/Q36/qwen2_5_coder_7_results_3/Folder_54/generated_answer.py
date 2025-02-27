def filter_chars(s):
    for char in s[18:38]:
        if ')' < char < 'P':
            s = s.replace(char, '')
    return s