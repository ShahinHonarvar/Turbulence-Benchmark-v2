def remove_repeat_chars(s):
    repeat_chars = [char for char in s[86:99] if s[86:99].count(char) > 1]
    repeat_chars = set(repeat_chars)
    return ''.join([char for char in s if char not in repeat_chars or char not in s[86:99]])