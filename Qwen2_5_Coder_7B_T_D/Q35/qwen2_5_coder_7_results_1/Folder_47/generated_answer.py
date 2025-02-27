def remove_repeat_chars(s):
    chars = list(s)
    repeat_chars = set()
    for i in range(29, 53):
        if chars[i] in repeat_chars:
            chars[i] = ''
        elif chars[i] in chars[:29] or chars[i] in chars[53:]:
            repeat_chars.add(chars[i])
        else:
            chars[i] = ''
    return ''.join(chars)