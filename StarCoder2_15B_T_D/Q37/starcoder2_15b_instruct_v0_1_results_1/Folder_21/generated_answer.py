def filter_chars(string):
    filtered_chars = [char for char in string if char < 'Q' or char > 'h']
    return ''.join(filtered_chars)