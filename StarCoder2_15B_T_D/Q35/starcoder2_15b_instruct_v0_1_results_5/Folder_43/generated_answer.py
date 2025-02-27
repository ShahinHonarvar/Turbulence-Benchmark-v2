def remove_repeat_chars(text):
    chars = list(text)
    for i in range(10, 28):
        if chars[i] in chars[i + 1:]:
            chars.pop(i)
            i -= 1
    return ''.join(chars)