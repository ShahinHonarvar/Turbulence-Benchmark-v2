def remove_repeat_chars(s):
    t = s[70:98]
    repeat_chars = {char for char in t if t.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))