def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1 and 17 < string.index(char) < 88:
            string = string.replace(char, '')
    return string