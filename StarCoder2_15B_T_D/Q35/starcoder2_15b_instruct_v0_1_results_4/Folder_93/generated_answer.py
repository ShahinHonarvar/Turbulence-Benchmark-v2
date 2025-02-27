def remove_repeat_chars(text: str) -> str:
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count > 1 and 57 < text.index(char) < 85:
            text = text.replace(char, '')
    return text