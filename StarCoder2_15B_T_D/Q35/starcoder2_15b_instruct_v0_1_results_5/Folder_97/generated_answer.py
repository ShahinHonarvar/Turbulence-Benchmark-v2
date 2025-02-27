def remove_repeat_chars(string):
    char_count = {}
    for char in string[34:69]:
        char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count > 1:
            string = string.replace(char, '')
    return string