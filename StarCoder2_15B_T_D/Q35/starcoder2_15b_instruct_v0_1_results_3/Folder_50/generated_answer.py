def remove_repeat_chars(text):
    char_counts = {}
    for char in text[13:76]:
        char_counts[char] = char_counts.get(char, 0) + 1
    result = []
    for char in text:
        if char_counts[char] == 1 or char not in text[13:76]:
            result.append(char)
    return ''.join(result)