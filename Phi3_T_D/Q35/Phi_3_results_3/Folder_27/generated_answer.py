def remove_repeat_chars(s):
    indices = range(86, 90)
    chars_to_remove = {char for char in s[indices[0]:indices[-1]] if s.count(char, indices[0], indices[-1]) > 1}
    return ''.join([char for char in s if char not in chars_to_remove])