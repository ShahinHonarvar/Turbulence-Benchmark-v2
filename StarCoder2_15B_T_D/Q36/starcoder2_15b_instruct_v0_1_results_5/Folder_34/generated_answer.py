def filter_chars(string):
    char_list = list(string)
    for i in range(10, 79):
        if char_list[i] > '?' and char_list[i] < 'm':
            char_list = [c for c in char_list if c != char_list[i]]
    return ''.join(char_list)