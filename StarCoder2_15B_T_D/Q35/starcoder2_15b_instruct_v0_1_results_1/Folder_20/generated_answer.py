def remove_repeat_chars(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count > 1 and 27 < ord(char) < 96:
            text = text.replace(char, '')
    return text