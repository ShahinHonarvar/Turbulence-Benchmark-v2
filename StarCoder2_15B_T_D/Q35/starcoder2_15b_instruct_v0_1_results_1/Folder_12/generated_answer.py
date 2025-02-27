def remove_repeat_chars(text):
    chars = list(text)
    for i, c in enumerate(text[16:87]):
        if c in text[16:i] + text[i + 1:87]:
            chars[i] = ''
    return ''.join(chars)