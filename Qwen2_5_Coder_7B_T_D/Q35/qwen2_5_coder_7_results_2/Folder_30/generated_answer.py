def remove_repeat_chars(s):
    indices = list(range(22, 24))
    repeat_chars = [s[i] for i in indices if s.count(s[i]) > 1]
    repeat_chars = list(set(repeat_chars))
    for char in repeat_chars:
        s = s.replace(char, '')
    return s