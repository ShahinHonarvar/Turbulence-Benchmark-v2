def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char in char_counts:
        if char_counts[char] > 1 and 355 < string.index(char) < 988:
            string = string.replace(char, '')
    return string