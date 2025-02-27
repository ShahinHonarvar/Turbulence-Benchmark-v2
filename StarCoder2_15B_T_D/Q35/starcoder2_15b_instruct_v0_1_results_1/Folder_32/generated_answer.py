def remove_repeat_chars(text):
    count = {}
    for c in text[86:90]:
        count[c] = count.get(c, 0) + 1
    for c in count:
        if count[c] > 1:
            text = text.replace(c, '')
    return text