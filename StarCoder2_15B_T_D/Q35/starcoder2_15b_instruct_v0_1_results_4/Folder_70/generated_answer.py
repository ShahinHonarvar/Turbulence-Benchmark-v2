def remove_repeat_chars(text):
    counts = {}
    for c in text:
        counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1:
            text = text.replace(c, '')
    return text