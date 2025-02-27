def remove_repeat_chars(text):
    char_count = {}
    for i, char in enumerate(text):
        if 44 < i < 91:
            char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count > 1:
            text = text.replace(char, '')
    return text