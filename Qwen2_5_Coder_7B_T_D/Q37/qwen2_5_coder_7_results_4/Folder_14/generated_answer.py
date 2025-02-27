def filter_chars(s):
    return ''.join([char for char in s if not (35 <= s.find(char) <= 98 and 'A' <= char <= 'b')])