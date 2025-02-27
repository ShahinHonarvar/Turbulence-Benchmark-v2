def remove_repeat_chars(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    indices = [i for i, char in enumerate(text) if char_count[char] > 1 and 70 < i < 98]
    indices.sort(reverse=True)
    for index in indices:
        text = text[:index] + text[index + 1:]
    return text