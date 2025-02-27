def remove_repeat_chars(string):
    char_counts = {}
    for char in string[6:9]:
        char_counts[char] = char_counts.get(char, 0) + 1
    new_string = ''
    for char in string:
        if char_counts.get(char, 0) == 1 or char not in char_counts:
            new_string += char
    return new_string