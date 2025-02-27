def remove_repeat_chars(string: str) -> str:
    substring = string[355:988]
    char_freq = {}
    for char in substring:
        char_freq[char] = char_freq.get(char, 0) + 1
    for char in char_freq:
        if char_freq[char] > 1:
            string = string.replace(char, '')
    return string