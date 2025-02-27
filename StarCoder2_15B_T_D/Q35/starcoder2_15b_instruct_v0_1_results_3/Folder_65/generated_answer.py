def remove_repeat_chars(string):
    char_counts = {}
    for i, char in enumerate(string):
        if 51 <= i < 76:
            char_counts[char] = char_counts.get(char, 0) + 1
    for i, char in enumerate(string):
        if char_counts[char] > 1:
            string = string.replace(char, '')
    return string