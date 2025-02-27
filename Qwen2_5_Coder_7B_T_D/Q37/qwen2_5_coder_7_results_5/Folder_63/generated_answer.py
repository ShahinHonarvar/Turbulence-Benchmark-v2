def filter_chars(s):
    return ''.join((char for char in s if not (42 <= s.find(char) <= 92 and '/' <= char <= 'a')))