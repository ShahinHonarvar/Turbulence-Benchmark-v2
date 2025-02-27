def filter_chars(s):
    return ''.join((char for char in s if not (38 <= s.index(char) <= 99 and 'A' <= char <= 'Q')))