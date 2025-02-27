def filter_chars(s):
    if len(s) <= 96:
        chars_to_remove = set(s[max(51, len(s) - 1):min(96, len(s)) + 1])
    else:
        chars_to_remove = set(s[51:97])
    chars_to_remove = {char for char in chars_to_remove if 'X' <= char <= 'p'}
    return ''.join((char for char in s if char not in chars_to_remove))