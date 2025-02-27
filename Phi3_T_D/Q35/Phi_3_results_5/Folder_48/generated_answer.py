def remove_repeat_chars(s):
    start, end = (409, 502)
    chars_to_remove = {char for char in s[start:end] if s[start:end].count(char) > 1}
    return ''.join([char for char in s if char not in chars_to_remove])