def remove_repeat_chars(string):
    char_counts = {}
    for char in string[38:52]:
        char_counts[char] = string[38:52].count(char)
    for char, count in char_counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string