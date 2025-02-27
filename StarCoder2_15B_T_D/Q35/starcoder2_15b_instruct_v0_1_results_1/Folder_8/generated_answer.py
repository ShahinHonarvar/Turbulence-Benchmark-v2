def remove_repeat_chars(string: str) -> str:
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count > 1 and 45 < string.index(char) < 48:
            string = string.replace(char, '')
    return string