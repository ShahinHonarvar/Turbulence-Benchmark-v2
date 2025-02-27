def filter_chars(s):
    chars_to_remove = set('&' + 'abcdefghijklmnopqrstuvwxyz'[:22])
    return ''.join([char for char in s if s.index(char) < 12 or s.index(char) > 88 or char not in chars_to_remove])