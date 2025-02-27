def filter_chars(s):
    result = [char for char in s if not (31 <= s.index(char) <= 38 and ';' <= char <= 'g')]
    return ''.join(result)