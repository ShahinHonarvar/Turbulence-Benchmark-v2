def remove_repeat_chars(string: str) -> str:
    indices = [70, 98]
    char_counts = {}
    for char in string[indices[0]:indices[1]]:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string