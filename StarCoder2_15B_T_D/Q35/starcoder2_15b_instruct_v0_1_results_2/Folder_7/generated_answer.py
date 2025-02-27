def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char, count in char_counts.items():
        if count > 1 and 375 < string.index(char) < 926:
            string = string.replace(char, '')
    return string