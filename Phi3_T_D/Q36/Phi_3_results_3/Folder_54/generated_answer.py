def filter_chars(s):
    for char in s[18:38]:
        if ord(')') < ord(char) < ord('P'):
            s = s.replace(char, '')
    return s