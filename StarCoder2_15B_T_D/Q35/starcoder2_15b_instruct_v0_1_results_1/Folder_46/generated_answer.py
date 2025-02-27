def remove_repeat_chars(text):
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    for c in freq:
        if freq[c] > 1 and 10 < text.index(c) < 79:
            text = text.replace(c, '')
    return text