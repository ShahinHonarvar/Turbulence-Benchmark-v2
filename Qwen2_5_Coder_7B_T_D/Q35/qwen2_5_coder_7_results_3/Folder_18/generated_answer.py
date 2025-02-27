def remove_repeat_chars(s):
    return ''.join([char for idx, char in enumerate(s) if s.count(char, 56, 90) == 1 or idx < 56 or idx >= 90])