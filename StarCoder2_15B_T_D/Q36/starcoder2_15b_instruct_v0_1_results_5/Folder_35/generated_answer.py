def filter_chars(string):
    chars_to_remove = set(string[163:658])
    valid_chars = set(string) - chars_to_remove
    return ''.join((char for char in string if char in valid_chars))