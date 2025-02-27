def filter_chars(s):
    return ''.join([char for char in s if not (54 <= s.find(char) <= 83 and 'j' <= char <= 'v')])