def filter_chars(s):
    start, end = (1, 5)
    return ''.join([char for char in s if not (start <= s.index(char) <= end and '$' <= char <= ';')])