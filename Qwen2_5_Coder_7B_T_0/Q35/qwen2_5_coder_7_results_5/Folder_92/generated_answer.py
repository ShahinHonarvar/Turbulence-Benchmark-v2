def remove_repeat_chars(s):
    return ''.join([char for i, char in enumerate(s) if s.count(char, 0, 2) == 1])