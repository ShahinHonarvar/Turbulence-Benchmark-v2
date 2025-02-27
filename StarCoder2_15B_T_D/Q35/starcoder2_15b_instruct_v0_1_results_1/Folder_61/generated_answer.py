def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    for char, count in char_counts.items():
        if count > 1 and string.index(char) < 8:
            string = string.replace(char, '')
    return string