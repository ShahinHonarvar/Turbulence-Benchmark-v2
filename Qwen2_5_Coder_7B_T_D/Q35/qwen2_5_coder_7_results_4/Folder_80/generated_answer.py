def remove_repeat_chars(s):
    indices = list(range(57, 84))
    repeat_chars = [char for char in s[57:84] if s[57:84].count(char) > 1]
    repeat_chars = set(repeat_chars)
    result = ''.join([char for char in s if char not in repeat_chars])
    return result