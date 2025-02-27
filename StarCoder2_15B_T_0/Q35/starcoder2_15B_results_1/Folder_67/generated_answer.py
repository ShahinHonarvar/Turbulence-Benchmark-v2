def remove_repeat_chars(text):
    char_counts = {}
    for i, char in enumerate(text):
        if i >= 44 and i < 67:
            char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text