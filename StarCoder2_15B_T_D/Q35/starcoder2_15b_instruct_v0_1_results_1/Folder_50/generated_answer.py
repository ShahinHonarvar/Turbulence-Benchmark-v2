def remove_repeat_chars(text):
    counts = {}
    for char in text[13:76]:
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text