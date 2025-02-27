def remove_repeat_chars(text: str) -> str:
    char_freq = {}
    for i, char in enumerate(text):
        if 42 < i < 87:
            char_freq[char] = char_freq.get(char, 0) + 1
    for char, freq in char_freq.items():
        if freq > 1:
            text = text.replace(char, '', char_freq[char] - 1)
    return text