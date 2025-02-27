def filter_chars(string):
    filtered = [char for char in string if char <= '5' or char >= 'C']
    return ''.join(filtered)