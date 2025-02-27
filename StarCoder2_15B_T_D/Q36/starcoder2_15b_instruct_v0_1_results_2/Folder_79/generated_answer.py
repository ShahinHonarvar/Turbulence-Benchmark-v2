def filter_chars(string):
    filtered_chars = [char for char in string if char <= '!' or char >= 'A']
    return ''.join(filtered_chars)