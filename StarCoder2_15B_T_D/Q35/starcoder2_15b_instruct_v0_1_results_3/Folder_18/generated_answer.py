def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for i, char in enumerate(string):
        if char_counts[char] > 1 and 56 < i < 90:
            string = string.replace(char, '')
    return string