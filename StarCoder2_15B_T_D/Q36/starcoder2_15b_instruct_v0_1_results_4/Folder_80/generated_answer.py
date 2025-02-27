def filter_chars(string):
    filtered = [char for char in string if char <= 'J' or char >= 'X']
    return ''.join(filtered)