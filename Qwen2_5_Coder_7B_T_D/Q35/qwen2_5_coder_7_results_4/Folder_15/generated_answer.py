def remove_repeat_chars(s):
    return s[0:4] + ''.join([char for char in s[4:] if s[4:].count(char) == 0])