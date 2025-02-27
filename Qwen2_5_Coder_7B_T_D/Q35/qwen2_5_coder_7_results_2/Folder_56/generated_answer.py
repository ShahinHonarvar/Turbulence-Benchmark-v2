def remove_repeat_chars(s):
    chars = list(s)
    repeat_chars = set()
    for i in range(7, 9):
        if chars[i] in repeat_chars:
            chars[i] = ''
        else:
            repeat_chars.add(chars[i])
    return ''.join(chars)