def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('.'), ord('b') + 1) if 72 <= ord(i) <= 94])
    return ''.join([char for char in s if char not in chars_to_remove])