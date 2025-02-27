def remove_repeat_chars(s):
    if len(s) <= 93:
        return s
    t = s[73:93]
    chars_to_remove = {char for char in t if t.count(char) > 1}
    return ''.join([char for char in s if char not in chars_to_remove])