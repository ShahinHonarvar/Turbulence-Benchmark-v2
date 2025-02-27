def remove_repeat_chars(string):
    char_counts = {}
    for char in string[86:89]:
        char_counts[char] = string.count(char)
    for char, count in char_counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string