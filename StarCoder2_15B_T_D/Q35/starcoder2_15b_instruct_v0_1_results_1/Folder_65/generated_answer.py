def remove_repeat_chars(text: str) -> str:
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1 and 51 < text.index(char) < 76:
            text = text.replace(char, '')
    return text