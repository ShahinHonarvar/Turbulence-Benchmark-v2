def remove_repeat_chars(text):
    char_counts = {}
    for i, char in enumerate(text):
        if i >= 409 and i < 502:
            char_counts[char] = char_counts.get(char, 0) + 1
    for i, char in enumerate(text):
        if i >= 409 and i < 502 and (char_counts[char] > 1):
            text = text[:i] + text[i + 1:]
    return text