def remove_repeat_chars(string):
    char_counts = {}
    char_indices = {}
    for i, char in enumerate(string):
        if char not in char_counts:
            char_counts[char] = 0
            char_indices[char] = []
        char_counts[char] += 1
        char_indices[char].append(i)
    for char, count in char_counts.items():
        if count > 1 and 38 < min(char_indices[char]) < 81 < max(char_indices[char]):
            string = string.replace(char, '')
    return string