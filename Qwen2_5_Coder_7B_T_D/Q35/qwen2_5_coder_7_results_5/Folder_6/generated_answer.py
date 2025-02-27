def remove_repeat_chars(s):
    repeat_chars = [char for char in s[20:93] if s[20:93].count(char) > 1]
    repeat_chars = set(repeat_chars)
    result = [char for char in s if char not in repeat_chars]
    return ''.join(result)