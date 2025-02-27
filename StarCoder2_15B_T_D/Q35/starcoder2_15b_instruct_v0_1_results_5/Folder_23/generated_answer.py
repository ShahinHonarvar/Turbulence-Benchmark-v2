def remove_repeat_chars(text):
    char_counts = {}
    for i, char in enumerate(text):
        if i >= 20 and i < 36:
            char_counts[char] = char_counts.get(char, 0) + 1
    for char in char_counts:
        if char_counts[char] > 1:
            text = text.replace(char, '')
    return text