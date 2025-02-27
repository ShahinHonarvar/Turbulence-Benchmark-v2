def remove_repeat_chars(s):
    target = s[20:43]
    repeat_chars = {char for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))