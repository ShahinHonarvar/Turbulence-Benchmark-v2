def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 669 or i >= 888 or (char <= 'B' or char >= 'Y')]
    return ''.join(filtered_chars)