def filter_chars(input_str):
    return ''.join((char for i, char in enumerate(input_str) if (i < 521 or i > 722) or (char < '>' or char > '_')))