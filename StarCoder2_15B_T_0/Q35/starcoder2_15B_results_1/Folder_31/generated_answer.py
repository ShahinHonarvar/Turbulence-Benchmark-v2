def remove_repeat_chars(string):
    char_counts = {}
    for i, char in enumerate(string):
        if i in range(33, 78):
            char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string