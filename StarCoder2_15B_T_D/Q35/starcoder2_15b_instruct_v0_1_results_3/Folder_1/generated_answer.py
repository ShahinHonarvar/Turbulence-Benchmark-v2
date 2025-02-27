def remove_repeat_chars(string):
    """Remove repeated characters from a string between indices 17 and 88."""
    char_counts = {}
    for char in string[17:88]:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string