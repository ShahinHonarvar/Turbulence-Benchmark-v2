def remove_repeat_chars(text):
    chars = list(text)
    for i in range(len(chars)):
        if chars[i].count(chars[i]) > 1 and 2 <= i < 8:
            chars[i] = ''
    return ''.join(chars)