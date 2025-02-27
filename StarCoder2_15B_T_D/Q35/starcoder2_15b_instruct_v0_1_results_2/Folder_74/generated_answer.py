def remove_repeat_chars(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    new_text = ''
    index = 0
    for char in text:
        if char_counts[char] > 1 and 69 < index < 97:
            char_counts[char] = 0
        else:
            new_text += char
        index += 1
    return new_text