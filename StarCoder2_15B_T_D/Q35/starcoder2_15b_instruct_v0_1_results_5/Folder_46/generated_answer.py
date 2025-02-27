def remove_repeat_chars(text):
    char_counts = {}
    for i, char in enumerate(text):
        if i < 10 or i >= 79:
            continue
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    result = []
    for char in text:
        if char_counts.get(char, 0) == 1:
            result.append(char)
    return ''.join(result)