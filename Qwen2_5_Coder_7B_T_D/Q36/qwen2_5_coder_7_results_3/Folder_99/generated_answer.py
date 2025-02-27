def filter_chars(s):
    target_chars = 'c'
    return ''.join([char for char in s if 476 < s.index(char) < 948 and char not in target_chars or (476 < s.index(char) < 948 and char in target_chars)])