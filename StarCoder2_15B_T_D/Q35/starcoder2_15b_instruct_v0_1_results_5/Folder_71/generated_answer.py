def remove_repeat_chars(text):
    indices = [i for i, c in enumerate(text) if 20 < i < 35]
    counts = {c: indices.count(c) for c in set(text[20:35])}
    repeated_chars = [c for c, count in counts.items() if count > 1]
    for char in repeated_chars:
        text = text.replace(char, '')
    return text