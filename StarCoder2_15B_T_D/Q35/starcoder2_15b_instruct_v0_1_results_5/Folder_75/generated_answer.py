def remove_repeat_chars(text):
    count = {}
    for i, c in enumerate(text):
        if i >= 20 and i < 51:
            count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] > 1:
            text = text.replace(c, '')
    return text