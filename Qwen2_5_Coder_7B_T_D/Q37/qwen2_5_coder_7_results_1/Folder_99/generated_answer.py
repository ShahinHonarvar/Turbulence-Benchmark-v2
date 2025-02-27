def filter_chars(s):
    filtered_chars = [char for index, char in enumerate(s) if index < 373 or index > 901 or (not 'T' <= char <= 'h')]
    return ''.join(filtered_chars)