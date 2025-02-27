def filter_chars(s):
    return ''.join((char for char in s if not (29 <= s.index(char) <= 97 and '-' <= char <= 'n')))