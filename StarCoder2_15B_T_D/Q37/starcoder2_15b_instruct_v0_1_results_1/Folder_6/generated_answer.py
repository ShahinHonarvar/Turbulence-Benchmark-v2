def filter_chars(string):
    filtered_chars = [char for char in string if char < 'c' or char > 'n' or string.index(char) < 13 or (string.index(char) > 28)]
    return ''.join(filtered_chars)