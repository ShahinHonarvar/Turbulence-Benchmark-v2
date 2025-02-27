def remove_repeat_chars(s):
    target = s[21:51]
    chars_to_remove = {char for char in target if target.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))