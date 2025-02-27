def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if (i < 722 or i > 832) or (char < 'K' or char > 'm')]
    return ''.join(filtered_chars)