def remove_repeat_chars(text: str) -> str:
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count > 1 and 409 < text.index(char) < 502:
            text = text.replace(char, '')
    return text