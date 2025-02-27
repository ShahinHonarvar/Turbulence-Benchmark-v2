def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 10 or i >= 15 or char <= 't' or (char >= 'v')]
    return ''.join(filtered_chars)