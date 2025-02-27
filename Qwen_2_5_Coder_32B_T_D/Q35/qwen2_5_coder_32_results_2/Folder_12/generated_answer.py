def remove_repeat_chars(s):
    if len(s) <= 88:
        return s
    segment = s[17:87]
    repeat_chars = {char for char in segment if segment.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))