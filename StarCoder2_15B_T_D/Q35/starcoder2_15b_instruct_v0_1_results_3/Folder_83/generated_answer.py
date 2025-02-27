def remove_repeat_chars(text: str) -> str:
    frequencies = {}
    for i, char in enumerate(text):
        if i < 100 or i >= 200:
            continue
        frequencies[char] = frequencies.get(char, 0) + 1
    for char, freq in frequencies.items():
        if freq > 1:
            text = text.replace(char, '')
    return text