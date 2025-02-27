def remove_repeat_chars(string: str) -> str:
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1 and 10 < string.index(char) < 79:
            string = string.replace(char, '')
    return string