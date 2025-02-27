def remove_repeat_chars(text):
    char_counts = {}
    for i, c in enumerate(text):
        if i >= 39 and i < 43:
            char_counts[c] = char_counts.get(c, 0) + 1
    for c, count in char_counts.items():
        if count > 1:
            text = text.replace(c, '')
    return text