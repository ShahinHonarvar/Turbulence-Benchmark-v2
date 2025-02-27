def filter_chars(string):
    return ''.join((char for char in string if char <= '5' or char >= 'C'))