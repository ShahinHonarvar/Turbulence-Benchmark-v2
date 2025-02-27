def remove_repeat_chars(text):
    char_counts = {}
    for i, char in enumerate(text):
        if i < 48 or i >= 76:
            continue
        char_counts[char] = char_counts.get(char, 0) + 1
    result = []
    for i, char in enumerate(text):
        if char_counts[char] > 1:
            if i < 48 or i >= 76:
                result.append(char)
            else:
                char_counts[char] -= 1
        else:
            result.append(char)
    return ''.join(result)