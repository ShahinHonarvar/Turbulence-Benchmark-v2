def remove_repeat_chars(string):
    char_counts = {}
    for char in string[18:60]:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in string:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)