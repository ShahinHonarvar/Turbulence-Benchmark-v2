def remove_repeat_chars(s):
    t = s[49:76]
    repeats = {char for char in t if t.count(char) > 1}
    return ''.join((char for char in s if char not in repeats))