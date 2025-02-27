def filter_chars(s):
    for char in s[50:92]:
        if 'A' < char < 'Q':
            s = s.replace(char, '')
    return s