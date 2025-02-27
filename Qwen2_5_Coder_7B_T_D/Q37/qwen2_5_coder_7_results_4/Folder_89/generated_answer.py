def filter_chars(s):
    chars_to_remove = set('!@')
    return ''.join([char for i, char in enumerate(s) if i < 11 or i > 32 or char not in chars_to_remove])