def remove_repeat_chars(s):
    target = s[2:5]
    repeats = {char for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in repeats))