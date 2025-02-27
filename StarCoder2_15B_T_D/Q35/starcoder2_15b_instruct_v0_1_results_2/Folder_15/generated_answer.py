def remove_repeat_chars(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1 and text.index(char) >= 0 and (text.index(char) < 4):
            text = text.replace(char, '')
    return text