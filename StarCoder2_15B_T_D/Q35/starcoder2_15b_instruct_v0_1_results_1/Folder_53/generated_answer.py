def remove_repeat_chars(text):
    counts = {}
    for i, c in enumerate(text):
        if i >= 200 and i < 202:
            counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1:
            text = text.replace(c, '')
    return text