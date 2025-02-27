def remove_repeat_chars(s):
    if len(s) <= 9:
        return s
    sub = s[8:9]
    chars_to_remove = set()
    for char in sub:
        if s.count(char, 8, 9) > 1:
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))