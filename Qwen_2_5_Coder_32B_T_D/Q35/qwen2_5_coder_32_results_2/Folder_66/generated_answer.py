def remove_repeat_chars(s):
    if len(s) <= 77:
        return s
    sub = s[12:76]
    repeats = {char for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in repeats))