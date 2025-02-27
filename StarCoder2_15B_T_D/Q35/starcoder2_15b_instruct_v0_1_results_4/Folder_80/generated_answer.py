def remove_repeat_chars(text):
    char_counts = {}
    for char in text[57:84]:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = [char for char, count in char_counts.items() if count > 1]
    new_text = ''.join((char for char in text if char not in repeated_chars))
    return new_text