def remove_repeat_chars(s):
    if len(s) <= 88:
        return s
    t = s[56:88]
    repeat_chars = {char for char in t if t.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))