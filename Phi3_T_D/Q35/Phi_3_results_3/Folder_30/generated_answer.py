def remove_repeat_chars(s):
    repeated_chars = {char for char in s[22:24] if s[22:24].count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars or char not in s[22:24]))