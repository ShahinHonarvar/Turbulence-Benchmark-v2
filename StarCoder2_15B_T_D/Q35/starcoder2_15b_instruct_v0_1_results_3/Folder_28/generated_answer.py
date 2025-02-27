def remove_repeat_chars(text):
    char_counts = {}
    for i, char in enumerate(text):
        if i < 86 or i >= 99:
            continue
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text