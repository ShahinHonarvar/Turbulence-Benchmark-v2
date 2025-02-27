def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 421 or i >= 854 or char <= 'D' or (char >= 'J')]
    return ''.join(filtered_chars)