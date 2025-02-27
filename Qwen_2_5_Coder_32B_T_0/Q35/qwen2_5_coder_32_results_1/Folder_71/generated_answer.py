def remove_repeat_chars(s):
    t = s[20:35]
    chars_to_remove = {char for char in t if t.count(char) > 1}
    return ''.join((char for char in s if char not in chars_to_remove))