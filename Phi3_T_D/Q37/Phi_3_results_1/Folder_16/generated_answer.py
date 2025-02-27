from string import ascii_uppercase

def filter_chars(s):
    for char in ascii_uppercase:
        if 'D' <= char <= 'Y':
            s = s.replace(char, '')
    return s[225:382]