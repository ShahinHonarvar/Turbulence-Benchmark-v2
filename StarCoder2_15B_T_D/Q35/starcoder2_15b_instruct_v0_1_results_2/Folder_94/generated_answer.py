def remove_repeat_chars(string: str) -> str:
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    for char, count in char_counts.items():
        if count > 1 and 42 < string.index(char) < 87:
            string = string.replace(char, '')
    return string