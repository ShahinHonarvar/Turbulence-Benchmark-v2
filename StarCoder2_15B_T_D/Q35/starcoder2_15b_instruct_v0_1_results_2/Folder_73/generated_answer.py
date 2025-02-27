def remove_repeat_chars(text):
    counts = {}
    for i, c in enumerate(text):
        if 10 <= i < 76:
            counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1:
            text = text.replace(c, '')
    return text