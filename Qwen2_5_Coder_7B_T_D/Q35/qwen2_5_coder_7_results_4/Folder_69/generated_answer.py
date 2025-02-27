def remove_repeat_chars(s):
    indices = s[39:43]
    repeat_chars = [char for char in indices if indices.count(char) > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s