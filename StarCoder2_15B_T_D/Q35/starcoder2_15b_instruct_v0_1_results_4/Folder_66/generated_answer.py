def remove_repeat_chars(s: str) -> str:
    """
    Removes repeated characters from the string's' between indices 11 and 76,
    while preserving the order of all characters in the string.
    """
    char_counts = {}
    for idx, char in enumerate(s[11:76]):
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    filtered_chars = []
    for idx, char in enumerate(s):
        if char in char_counts and char_counts[char] > 1 and (11 <= idx < 76):
            char_counts[char] -= 1
        else:
            filtered_chars.append(char)
    return ''.join(filtered_chars)