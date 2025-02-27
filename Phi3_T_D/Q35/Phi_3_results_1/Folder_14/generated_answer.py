def remove_repeat_chars(s):
    unique_chars = set(s[2:5])
    return ''.join((char for char in s if char not in unique_chars))