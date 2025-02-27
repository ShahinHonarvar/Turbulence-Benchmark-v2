def filter_chars(string):
    return ''.join([char for char in string if char < 'A' or char >= 'i' or (char >= 'A' and char < 'A' + 27) or (char >= 'i' + 75 and char < 'i')])