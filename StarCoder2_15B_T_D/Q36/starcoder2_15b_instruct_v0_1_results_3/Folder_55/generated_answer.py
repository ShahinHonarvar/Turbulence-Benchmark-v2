def filter_chars(string):
    filtered = [char for char in string if char <= 'Y' or char >= 's' or char not in string[3:5]]
    return ''.join(filtered)