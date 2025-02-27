def filter_chars(s):
    chars_to_remove = {char for idx, char in enumerate(s) if 515 <= idx <= 538 and '+' <= char <= '}'}
    return ''.join((char for char in s if char not in chars_to_remove))