def remove_repeat_chars(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    indices_to_remove = []
    for i, char in enumerate(text):
        if char_count[char] > 1 and 33 < i < 78:
            indices_to_remove.append(i)
    return ''.join((char for i, char in enumerate(text) if i not in indices_to_remove))