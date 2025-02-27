def remove_repeat_chars(input_string):
    char_counts = {}
    for i, char in enumerate(input_string):
        if char not in char_counts:
            char_counts[char] = []
        char_counts[char].append(i)
    for char, indices in char_counts.items():
        if len(indices) > 1 and 45 < indices[0] < 48:
            input_string = input_string.replace(char, '')
    return input_string