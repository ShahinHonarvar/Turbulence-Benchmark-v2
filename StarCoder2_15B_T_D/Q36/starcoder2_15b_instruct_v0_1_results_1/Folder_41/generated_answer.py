def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 81 or i >= 89 or char <= 'f' or (char >= '{')]
    return ''.join(filtered_chars)