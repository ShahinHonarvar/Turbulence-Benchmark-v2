def remove_repeat_chars(text):
    if len(text) <= 50 or len(text) <= 200:
        return text
    char_counts = {}
    for i, char in enumerate(text):
        if 50 < i < 200:
            char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text