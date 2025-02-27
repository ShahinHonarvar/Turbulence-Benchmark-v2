def remove_repeat_chars(text):
    chars = list(text)
    char_counts = {}
    for i in range(73, 84):
        char = chars[i]
        char_counts[char] = char_counts.get(char, 0) + 1
    for i in range(73, 84):
        char = chars[i]
        if char_counts[char] > 1:
            chars[i] = ''
    return ''.join(chars)