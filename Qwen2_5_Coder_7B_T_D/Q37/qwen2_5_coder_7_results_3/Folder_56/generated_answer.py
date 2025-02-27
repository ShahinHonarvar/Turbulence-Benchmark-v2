def filter_chars(s):
    return ''.join([char for char in s if not (71 <= ord(char) <= 94 and 'K' <= char <= 'a')])