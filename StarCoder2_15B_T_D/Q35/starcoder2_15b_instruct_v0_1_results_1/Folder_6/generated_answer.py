def remove_repeat_chars(s: str) -> str:
    char_counts = {}
    for i, char in enumerate(s):
        if i >= 20 and i < 93:
            char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = [char for char, count in char_counts.items() if count > 1]
    output = ''
    for char in s:
        if char not in repeated_chars:
            output += char
    return output