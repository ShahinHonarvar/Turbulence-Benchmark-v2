def remove_repeat_chars(s):
    return ''.join([char for idx, char in enumerate(s) if s.count(char, 0, 3) < 2])