def remove_repeat_chars(s):
    return ''.join([char for i, char in enumerate(s) if (i < 73 or i >= 84) or s.count(char, 73, 84) == 1])