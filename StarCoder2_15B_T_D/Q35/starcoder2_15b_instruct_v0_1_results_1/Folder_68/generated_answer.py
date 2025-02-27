def remove_repeat_chars(s: str) -> str:
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1 and 0 < s.index(char) < 9}
    new_string = ''
    for char in s:
        if char not in repeated_chars:
            new_string += char
    return new_string