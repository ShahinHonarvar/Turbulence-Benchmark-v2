def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    indices_to_remove = []
    for i, char in enumerate(string):
        if char_counts[char] > 1 and 50 < i < 92:
            indices_to_remove.append(i)
    for index in sorted(indices_to_remove, reverse=True):
        del string[index]
    return string