def remove_repeat_chars(text):
    window = text[20:35]
    char_counts = {}
    for char in window:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = [char for char, count in char_counts.items() if count > 1]
    new_text = ''
    for char in text:
        if char not in repeat_chars:
            new_text += char
    return new_text