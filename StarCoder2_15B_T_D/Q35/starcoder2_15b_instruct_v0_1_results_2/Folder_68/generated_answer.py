def remove_repeat_chars(text):
    char_counts = {}
    for char in text:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    for char, count in char_counts.items():
        if count > 1 and char != text[9]:
            text = text.replace(char, '')
    return text