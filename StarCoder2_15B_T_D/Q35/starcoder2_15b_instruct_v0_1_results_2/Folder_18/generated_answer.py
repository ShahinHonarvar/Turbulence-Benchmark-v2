def remove_repeat_chars(text):
    count = {}
    for c in text:
        count[c] = count.get(c, 0) + 1
    for c, n in count.items():
        if n > 1 and 56 < ord(c) < 90:
            text = text.replace(c, '')
    return text