def remove_repeat_chars(s):
    repeat_chars = [char for i, char in enumerate(s) if 62 < i < 96 and s.count(char) > 1]
    result = ''.join((char for char in s if char not in repeat_chars))
    return result