def filter_chars(s):
    return ''.join((char for char in s if not (521 <= s.find(char) <= 722 and '>' <= char <= '_')))