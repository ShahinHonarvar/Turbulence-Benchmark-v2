def remove_repeat_chars(string):
    new_string = ''
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] > 1 and 50 < string.index(char) < 92:
            continue
        else:
            new_string += char
    return new_string