def filter_chars(string):
    filtered_chars = [char for char in string if char <= 'S' or char >= '[']
    return ''.join(filtered_chars)