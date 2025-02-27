def filter_chars(string):
    for i in range(29, 33):
        if ord(string[i]) > ord('%') and ord(string[i]) < ord('a'):
            string = ''.join(filter(lambda x: x != string[i], string))
    return string