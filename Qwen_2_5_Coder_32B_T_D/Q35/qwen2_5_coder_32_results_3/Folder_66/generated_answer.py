def remove_repeat_chars(s):
    target_area = s[12:76]
    repeat_chars = {char for char in target_area if target_area.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))