def filter_chars(string):
    filtered = [char for char in string if char < 'A' or char > 'Q' or string.index(char) < 38 or (string.index(char) > 99)]
    return ''.join(filtered)