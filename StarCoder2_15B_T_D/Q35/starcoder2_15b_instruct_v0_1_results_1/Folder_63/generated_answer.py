def remove_repeat_chars(text):
    count_chars = {}
    for c in text:
        count_chars[c] = count_chars.get(c, 0) + 1
    for c, count in count_chars.items():
        if count > 1 and 81 < text.index(c) < 86:
            text = text.replace(c, '')
    return text