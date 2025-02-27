def filter_chars(text):
    filtered_chars = [char for i, char in enumerate(text) if i < 90 or i >= 97 or char <= 'j' or (char >= 'w')]
    return ''.join(filtered_chars)