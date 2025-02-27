def remove_repeat_chars(s):
    if len(s) <= 85:
        return s
    sub = s[58:84]
    repeat_chars = {char for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))