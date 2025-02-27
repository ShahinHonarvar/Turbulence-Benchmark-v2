def remove_repeat_chars(s):
    sub = s[43:70]
    repeats = {char for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in repeats))