def filter_chars(s):
    result = [char for char in s if not (138 <= s.index(char) <= 920 and '6' <= char <= 'A')]
    return ''.join(result)