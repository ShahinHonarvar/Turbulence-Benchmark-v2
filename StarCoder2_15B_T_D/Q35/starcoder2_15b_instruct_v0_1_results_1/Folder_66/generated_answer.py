def remove_repeat_chars(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    for i, char in enumerate(text):
        if char_counts[char] > 1 and 11 < i < 76:
            text = text.replace(char, '')
    return text