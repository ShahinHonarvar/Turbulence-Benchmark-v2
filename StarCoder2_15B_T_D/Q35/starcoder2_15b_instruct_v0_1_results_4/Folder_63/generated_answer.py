def remove_repeat_chars(string: str) -> str:
    substring = string[81:86]
    char_frequency = {}
    for char in substring:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    for char, frequency in char_frequency.items():
        if frequency > 1:
            string = string.replace(char, '')
    return string