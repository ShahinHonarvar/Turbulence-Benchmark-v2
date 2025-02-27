def remove_repeat_chars(text):
    counted = {}
    for i, c in enumerate(text):
        if 72 < i < 93:
            counted[c] = counted.get(c, 0) + 1
    for key, value in list(counted.items()):
        if value > 1:
            text = text.replace(key, '')
    return text