def filter_chars(string):
    string_list = list(string)
    for i in range(14, 75):
        if ord(string_list[i]) > ord('9') and ord(string_list[i]) < ord('K'):
            string_list.pop(i)
            i -= 1
    return ''.join(string_list)