def remove_repeat_chars(text):
    chars = list(text)
    char_counts = dict()
    for i, char in enumerate(chars):
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    for char, count in char_counts.items():
        if count > 1 and 0 < text.index(char) < 8:
            while char in chars:
                chars.remove(char)
    return ''.join(chars)