def remove_repeat_chars(string):
    char_count = {}
    for char in string[72:93]:
        char_count[char] = char_count.get(char, 0) + 1
    new_string = ''
    for char in string:
        if char_count[char] == 1 or char not in char_count:
            new_string += char
    return new_string