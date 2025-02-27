def remove_repeat_chars(text):
    count = {}
    for c in text[450:905]:
        count[c] = count.get(c, 0) + 1
    chars = [c for c in text if count[c] == 1]
    return ''.join(chars)