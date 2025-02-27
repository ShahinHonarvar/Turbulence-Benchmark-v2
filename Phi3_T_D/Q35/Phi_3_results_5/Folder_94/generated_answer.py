def remove_repeat_chars(s):
    start, end = (42, 88)
    chars_to_remove = {char for char in s[start:end] if s.count(char, start, end) > 1}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) < start or s.rindex(char) > end))