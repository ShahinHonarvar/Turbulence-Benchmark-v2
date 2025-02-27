def remove_repeat_chars(s):
    chars = list(s)
    for i in range(103, 802):
        if chars[i] in s[i + 1:]:
            chars[i] = ''
    return ''.join(chars)