def remove_repeat_chars(s):
    target_chars = set(s[462:995])
    return ''.join([char for char in s if char not in target_chars or s[462:995].count(char) == 1])