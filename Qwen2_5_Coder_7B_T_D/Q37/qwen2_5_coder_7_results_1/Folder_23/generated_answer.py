def filter_chars(s):
    return ''.join([char for char in s if not (51 <= s.find(char) <= 77 and 'V' <= char <= 'Y')])