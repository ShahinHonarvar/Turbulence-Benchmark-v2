def remove_repeat_chars(s):
    chars = set(s[1:5])
    repeat_chars = {char for char in chars if s[1:5].count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))