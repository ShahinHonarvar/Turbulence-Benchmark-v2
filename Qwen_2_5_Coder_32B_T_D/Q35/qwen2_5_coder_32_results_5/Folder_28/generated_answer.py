def remove_repeat_chars(s):
    if len(s) <= 99:
        return s
    target = s[87:99]
    repeat_chars = {char for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))