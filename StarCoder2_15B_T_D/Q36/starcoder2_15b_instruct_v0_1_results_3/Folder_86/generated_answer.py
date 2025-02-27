def filter_chars(string):
    filtered_chars = [char for char in string if char <= 'X' or char >= '}']
    return ''.join(filtered_chars)