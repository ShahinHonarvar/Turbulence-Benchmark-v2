def remove_repeat_chars(s):
    repeat_chars = [char for char in s[56:90] if s[56:90].count(char) > 1]
    repeat_chars = set(repeat_chars)
    return ''.join((char for char in s if char not in repeat_chars))