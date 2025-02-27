def filter_chars(s):
    chars_to_remove = set('fghijklmnop')
    return ''.join([char for char in s if char not in chars_to_remove or s.index(char) < 19 or s.index(char) > 32])