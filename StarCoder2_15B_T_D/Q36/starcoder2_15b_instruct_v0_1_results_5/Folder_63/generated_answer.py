def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if (i < 26 or i >= 80) or (char <= '<' or char >= '>')])