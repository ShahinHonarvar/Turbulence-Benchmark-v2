def filter_chars(s):
    pattern = '<' + '/' + 'abcdefghijklmnopqrstuvwxyz' + '>'[1:-1]
    return ''.join((char for char in s if not (42 <= s.find(char) <= 92 and char in pattern)))