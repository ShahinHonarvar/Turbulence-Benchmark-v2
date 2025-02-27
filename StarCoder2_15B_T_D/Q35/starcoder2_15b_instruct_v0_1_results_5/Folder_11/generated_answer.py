def remove_repeat_chars(string):
    char_count = {}
    for i, char in enumerate(string):
        if 48 < i < 76:
            char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count > 1:
            string = string.replace(char, '')
    return string