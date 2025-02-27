def remove_repeat_chars(string):
    char_count = {}
    for char in string[70:200]:
        char_count[char] = char_count.get(char, 0) + 1
    for char in char_count:
        if char_count[char] > 1:
            string = string.replace(char, '')
    return string