def remove_repeat_chars(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    for char in list(char_count.keys()):
        if char_count[char] > 1 and 476 < string.index(char) < 709:
            string = string.replace(char, '')
    return string