def filter_chars(text):
    return ''.join([char for i, char in enumerate(text) if i < 71 or i > 96 or char < '_' or (char > 'o')])