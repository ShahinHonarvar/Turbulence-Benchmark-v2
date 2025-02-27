def remove_repeat_chars(text):
    count = {}
    for c in text[56:88]:
        count[c] = count.get(c, 0) + 1
    for c in set(text[56:88]):
        if count[c] > 1:
            text = text.replace(c, '')
    return text