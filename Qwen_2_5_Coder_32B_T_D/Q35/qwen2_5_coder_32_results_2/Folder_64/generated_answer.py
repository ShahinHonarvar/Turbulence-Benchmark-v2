def remove_repeat_chars(s):
    chars = s[1:5]
    repeat_chars = {char for char in chars if chars.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))