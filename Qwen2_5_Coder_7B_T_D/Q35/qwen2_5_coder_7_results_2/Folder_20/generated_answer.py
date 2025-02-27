def remove_repeat_chars(s):
    repeat_chars = [char for i, char in enumerate(s) if i > 27 and i < 96 and (s.count(char) > 1)]
    return ''.join((char for char in s if char not in repeat_chars))