def remove_repeat_chars(s):
    return ''.join([char for index, char in enumerate(s) if char not in s[0:5] or s.count(char) == 1])