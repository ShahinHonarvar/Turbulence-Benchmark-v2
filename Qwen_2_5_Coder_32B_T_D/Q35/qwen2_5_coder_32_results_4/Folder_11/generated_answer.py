def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    target = s[49:76]
    to_remove = {char for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove))