def remove_repeat_chars(s):
    if len(s) <= 77:
        return s
    sub = s[13:76]
    chars_to_remove = {char for char in sub if sub.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))