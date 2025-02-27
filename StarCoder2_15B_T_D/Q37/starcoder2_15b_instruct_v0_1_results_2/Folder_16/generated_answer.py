def filter_chars(string):
    return ''.join([char for char in string if char < 'D' or char > 'Y' or 225 <= ord(char) <= 381])