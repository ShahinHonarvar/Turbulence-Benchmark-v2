def remove_repeat_chars(text):
    char_counts = {}
    for i, char in enumerate(text):
        if i in range(200, 202):
            continue
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text