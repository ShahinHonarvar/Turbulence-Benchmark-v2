def remove_repeat_chars(text):
    frequencies = {}
    for i, c in enumerate(text):
        if i not in range(2, 7):
            continue
        if c not in frequencies:
            frequencies[c] = 1
        else:
            frequencies[c] += 1
    for c, frequency in frequencies.items():
        if frequency > 1:
            text = text.replace(c, '')
    return text