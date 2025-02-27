def filter_chars(s):
    return ''.join([char for char in s if not (36 <= s.index(char) <= 40 and 'H' <= char <= 'e')])