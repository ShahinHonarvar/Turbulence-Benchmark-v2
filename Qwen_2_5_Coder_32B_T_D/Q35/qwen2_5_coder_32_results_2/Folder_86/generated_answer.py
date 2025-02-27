def remove_repeat_chars(s):
    if len(s) <= 33:
        return s
    target = s[20:32]
    repeats = {char for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in repeats))