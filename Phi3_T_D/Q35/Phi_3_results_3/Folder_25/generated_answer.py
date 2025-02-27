def remove_repeat_chars(s):
    chars_37_43 = set(s[37:43])
    for char in chars_37_43:
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s