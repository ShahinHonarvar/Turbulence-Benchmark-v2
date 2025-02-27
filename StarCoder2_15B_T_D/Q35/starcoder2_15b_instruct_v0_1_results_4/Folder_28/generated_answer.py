def remove_repeat_chars(string):
    char_list = list(string)
    for i in range(86, 99):
        if char_list.count(char_list[i]) > 1:
            while char_list[i] in char_list:
                char_list.remove(char_list[i])
    return ''.join(char_list)