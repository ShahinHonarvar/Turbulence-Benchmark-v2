def remove_repeat_chars(string):
    char_indices = {}
    for i, char in enumerate(string):
        if char in char_indices:
            if 32 < char_indices[char] < 44:
                string = string.replace(char, '')
        else:
            char_indices[char] = i
    return string