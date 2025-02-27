def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 18 or i >= 95 or char <= 'K' or (char >= 'a')])