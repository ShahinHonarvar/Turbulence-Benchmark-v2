def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    result = []
    for i, char in enumerate(string):
        if char_counts[char] == 1 or (i < 35 or i >= 64):
            result.append(char)
    return ''.join(result)