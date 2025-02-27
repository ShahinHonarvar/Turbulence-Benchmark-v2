def remove_repeat_chars(text):
    for c in set(text[36:54]):
        if text.count(c) > 1:
            text = text.replace(c, '')
    return text