def filter_chars(string):
    char_range = [ord(char) for char in string if 35 <= ord(char) <= 40]
    filtered_string = ''.join([char for char in string if char not in char_range])
    return filtered_string