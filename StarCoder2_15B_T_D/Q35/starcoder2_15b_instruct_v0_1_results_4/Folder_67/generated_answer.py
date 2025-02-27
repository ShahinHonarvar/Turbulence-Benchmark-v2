def remove_repeat_chars(text):
    char_freq = {}
    for i, c in enumerate(text):
        if i >= 44 and i < 67:
            char_freq[c] = char_freq.get(c, 0) + 1
    for c in char_freq:
        if char_freq[c] > 1:
            text = text.replace(c, '')
    return text