def remove_repeat_chars(s):
    a = s[13:70]
    repeats = {char for char in a if a.count(char) > 1}
    return ''.join([char for char in s if char not in repeats])