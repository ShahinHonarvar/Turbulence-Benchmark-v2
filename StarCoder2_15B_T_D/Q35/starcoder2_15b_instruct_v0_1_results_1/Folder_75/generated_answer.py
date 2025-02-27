def remove_repeat_chars(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    indices_to_remove = []
    for i, char in enumerate(text):
        if char_counts[char] > 1 and 20 < i < 51:
            indices_to_remove.append(i)
    new_text = ''
    for i, char in enumerate(text):
        if i not in indices_to_remove:
            new_text += char
    return new_text