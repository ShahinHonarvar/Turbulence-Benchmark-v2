def remove_repeat_chars(text):
    chars = list(text)
    for i in range(len(chars)):
        if chars[i] in chars[i + 1:]:
            del chars[i]
            i -= 1
    return ''.join(chars)