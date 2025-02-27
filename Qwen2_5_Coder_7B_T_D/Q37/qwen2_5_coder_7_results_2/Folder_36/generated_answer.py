def filter_chars(s):
    return ''.join([char for char in s if not (259 <= s.index(char) <= 502 and ',' <= char <= '3')])