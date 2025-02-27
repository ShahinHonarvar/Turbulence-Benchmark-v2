def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    new_string = ''
    for char in string:
        if char_counts[char] > 1:
            if char not in new_string:
                new_string += char
        else:
            new_string += char
    return new_string