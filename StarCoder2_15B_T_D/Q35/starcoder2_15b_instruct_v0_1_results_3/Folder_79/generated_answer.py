def remove_repeat_chars(text):
    characters = list(text)
    char_counts = {}
    for i, char in enumerate(characters):
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    for i, char in enumerate(characters):
        if char_counts[char] > 1 and i > 0 and (i < len(characters) - 1):
            del characters[i]
    return ''.join(characters)