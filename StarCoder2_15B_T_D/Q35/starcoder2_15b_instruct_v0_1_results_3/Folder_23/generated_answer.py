def remove_repeat_chars(text):
    chars = list(text)
    char_counts = {}
    for idx, char in enumerate(chars):
        if idx >= 20 and idx < 36:
            char_counts[char] = char_counts.get(char, 0) + 1
    for idx, char in enumerate(chars):
        if char_counts.get(char, 0) > 1 and idx >= 20 and (idx < 36):
            del chars[idx]
    return ''.join(chars)