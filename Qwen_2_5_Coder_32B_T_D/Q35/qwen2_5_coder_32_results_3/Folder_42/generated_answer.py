def remove_repeat_chars(s):
    if len(s) <= 60:
        return s
    target = s[18:60]
    repeating_chars = {char for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in repeating_chars))