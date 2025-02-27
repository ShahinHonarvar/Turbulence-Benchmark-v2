def filter_chars(string):
    for i in range(4, 8):
        if ord(string[i]) > ord('1') and ord(string[i]) < ord('J'):
            string = ''.join([c for c in string if c != string[i]])
    return string