def remove_repeat_chars(string):
    char_counts = {}
    for char in string[35:64]:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char, count in char_counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string