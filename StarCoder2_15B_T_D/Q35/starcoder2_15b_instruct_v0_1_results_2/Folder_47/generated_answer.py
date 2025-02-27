def remove_repeat_chars(text):
    count = {}
    for i, c in enumerate(text):
        if 29 <= i < 53:
            count[c] = count.get(c, 0) + 1
    for c, num in count.items():
        if num > 1:
            text = text.replace(c, '')
    return text