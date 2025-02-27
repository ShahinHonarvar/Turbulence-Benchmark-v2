def remove_repeat_chars(text):
    char_count = {}
    for i, c in enumerate(text):
        if 3 <= i < len(text) - 3:
            char_count[c] = char_count.get(c, 0) + 1
    for c, count in char_count.items():
        if count > 1:
            text = text.replace(c, '')
    return text