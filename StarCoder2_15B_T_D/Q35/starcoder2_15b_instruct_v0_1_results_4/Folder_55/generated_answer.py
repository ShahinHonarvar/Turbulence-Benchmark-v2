def remove_repeat_chars(string):
    char_counts = {}
    chars_to_remove = []
    for i, char in enumerate(string):
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
        if char_counts[char] > 1 and 10 < i < 100:
            chars_to_remove.append(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string