def remove_repeat_chars(string):
    char_counts = {}
    for i, char in enumerate(string):
        if 55 < i < 84:
            char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in string if char not in repeated_chars))