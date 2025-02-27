def filter_chars(s):
    return ''.join([char for char in s if not 1 <= s.index(char) <= 7 or not 'L' <= char <= 'a'])