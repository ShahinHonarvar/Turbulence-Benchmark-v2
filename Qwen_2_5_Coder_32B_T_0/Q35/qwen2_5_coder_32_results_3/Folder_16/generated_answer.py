def remove_repeat_chars(s):
    if len(s) <= 98:
        return s
    target = s[91:97]
    chars_to_remove = {char for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))