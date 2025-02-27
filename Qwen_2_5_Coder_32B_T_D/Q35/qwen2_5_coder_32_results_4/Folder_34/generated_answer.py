def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    sub = s[71:200]
    repeat_chars = {char for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))