def remove_repeat_chars(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in text:
        if char not in repeated_chars or char_counts[char] > 1:
            result.append(char)
        char_counts[char] -= 1
    return ''.join(result)