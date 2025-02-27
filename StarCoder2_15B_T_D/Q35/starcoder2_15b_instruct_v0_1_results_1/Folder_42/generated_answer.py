def remove_repeat_chars(text):
    char_counts = {}
    for i, c in enumerate(text):
        if 18 < i < 60:
            char_counts[c] = char_counts.get(c, 0) + 1
    for c in char_counts:
        if char_counts[c] > 1:
            text = text.replace(c, '')
    return text