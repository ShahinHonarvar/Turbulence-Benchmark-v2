def filter_chars(string):
    filtered_chars = [char for char in string if char < 'I' or char >= 'a']
    return ''.join(filtered_chars)