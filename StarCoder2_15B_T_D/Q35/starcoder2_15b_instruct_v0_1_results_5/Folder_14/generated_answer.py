def remove_repeat_chars(text: str) -> str:
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return ''.join([char for char in text if char_count[char] == 1 or text.index(char) < 2 or text.index(char) >= 5])