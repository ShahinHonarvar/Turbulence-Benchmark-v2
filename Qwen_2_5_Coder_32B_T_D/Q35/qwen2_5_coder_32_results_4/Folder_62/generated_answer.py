def remove_repeat_chars(s):
    if len(s) <= 92:
        return s
    t = s[50:92]
    repeat_chars = {char for char in t if t.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))