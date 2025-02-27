def remove_repeat_chars(s):
    if len(s) <= 60:
        return s
    target_area = s[18:60]
    repeat_chars = {char for char in target_area if target_area.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))