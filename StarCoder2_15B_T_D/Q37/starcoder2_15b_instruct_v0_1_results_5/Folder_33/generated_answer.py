def filter_chars(string):
    char_list = list(string)
    for i in range(len(char_list) - 1, -1, -1):
        if 722 <= i <= 832 and ord('K') <= ord(char_list[i]) <= ord('m'):
            del char_list[i]
    return ''.join(char_list)