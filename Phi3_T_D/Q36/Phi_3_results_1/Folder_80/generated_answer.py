def filter_chars(s):
    for char in s[54:92]:
        if 'J' < char < 'X':
            s = s.replace(char, '')
    return s