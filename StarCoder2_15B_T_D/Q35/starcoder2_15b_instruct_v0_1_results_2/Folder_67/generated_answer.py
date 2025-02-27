def remove_repeat_chars(text):
    counts = {}
    for i, char in enumerate(text):
        if i not in range(44, 67):
            continue
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text