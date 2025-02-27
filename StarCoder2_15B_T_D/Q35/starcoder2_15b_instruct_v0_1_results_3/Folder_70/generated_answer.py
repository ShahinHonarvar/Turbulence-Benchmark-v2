def remove_repeat_chars(text):
    indices = set()
    for i, c in enumerate(text):
        if 43 < i < 70 and c in text[43:i]:
            indices.add(i)
    return ''.join((c for i, c in enumerate(text) if i not in indices))