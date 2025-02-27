def remove_repeat_chars(text):
    counts = {}
    for c in text:
        counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1 and 20 < text.index(c) < len(text) - 51:
            text = text.replace(c, '')
    return text