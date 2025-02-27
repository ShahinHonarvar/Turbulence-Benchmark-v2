def filter_chars(s):
    chars_to_remove = set(';abc')
    return ''.join([char for char in s if char not in chars_to_remove if not (27 <= s.index(char) <= 29 and char in chars_to_remove)])