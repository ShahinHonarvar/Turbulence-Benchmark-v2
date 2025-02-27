def remove_repeat_chars(string):
    chars = {}
    for i, c in enumerate(string):
        if i >= 103 and i < 802:
            chars[c] = chars.get(c, 0) + 1
    for c, count in chars.items():
        if count > 1:
            string = string.replace(c, '')
    return string