def remove_repeat_chars(string: str) -> str:
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
    repeated_chars = set((char for char in char_freq if char_freq[char] > 1))
    result = ''
    for char in string:
        if char in repeated_chars:
            continue
        result += char
    return result