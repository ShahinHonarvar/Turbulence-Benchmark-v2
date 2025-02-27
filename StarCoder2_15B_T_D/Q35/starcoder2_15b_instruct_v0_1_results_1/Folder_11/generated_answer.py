def remove_repeat_chars(text: str) -> str:
    chars = list(text)
    char_counts = {}
    for i, char in enumerate(chars):
        if i in range(48, 76):
            char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            chars = [c for c in chars if c != char]
    return ''.join(chars)