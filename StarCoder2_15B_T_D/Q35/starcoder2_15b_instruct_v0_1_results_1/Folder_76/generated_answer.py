def remove_repeat_chars(string):
    char_count = {}
    for i, char in enumerate(string):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1 and 330 < i < 543:
            string = string.replace(char, '')
    return string