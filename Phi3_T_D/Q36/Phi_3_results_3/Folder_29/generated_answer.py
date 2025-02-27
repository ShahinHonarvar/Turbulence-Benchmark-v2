def filter_chars(string):
    excluded_chars = set([chr(i) for i in range(ord('H') + 1, ord('s')) if 46 < i < 68])
    altered_string = ''.join([char for char in string if char not in excluded_chars])
    return altered_string