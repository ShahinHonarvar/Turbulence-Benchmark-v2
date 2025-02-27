def remove_repeat_chars(s):
    repeat_chars = [char for char in s[3:9] if s[3:9].count(char) > 1]
    repeat_chars = set(repeat_chars)
    return ''.join((char for char in s if char not in repeat_chars))