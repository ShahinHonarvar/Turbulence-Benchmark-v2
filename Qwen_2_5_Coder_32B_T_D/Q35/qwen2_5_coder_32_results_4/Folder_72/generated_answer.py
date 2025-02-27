def remove_repeat_chars(s):
    if len(s) <= 70:
        return s
    target = s[13:70]
    repeats = {char for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in repeats))