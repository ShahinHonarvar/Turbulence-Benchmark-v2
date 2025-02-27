def remove_repeat_chars(s):
    repeat_chars = [char for char in s[51:76] if s[51:76].count(char) > 1]
    repeat_chars_set = set(repeat_chars)
    result = ''.join([char for char in s if char not in repeat_chars_set])
    return result