def remove_repeat_chars(s):
    indices = s[6:9]
    repeat_chars = [char for char in indices if indices.count(char) > 1]
    return ''.join((char for char in s if char not in repeat_chars))