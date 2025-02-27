def remove_repeat_chars(s):
    char_counts = {}
    for char in s[68:99]:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = [char for char in char_counts if char_counts[char] > 1]
    return ''.join([char for char in s if char not in repeated_chars])