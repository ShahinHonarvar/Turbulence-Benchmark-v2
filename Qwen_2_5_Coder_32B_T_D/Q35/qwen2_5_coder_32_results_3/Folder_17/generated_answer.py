def remove_repeat_chars(s):
    if len(s) <= 84:
        return s
    target_slice = s[73:84]
    repeat_chars = {char for char in target_slice if target_slice.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))