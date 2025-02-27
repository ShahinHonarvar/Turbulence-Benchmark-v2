def filter_chars(s):
    altered_string = [char for i, char in enumerate(s) if not (31 <= i <= 38 and ';' <= char <= 'g')]
    return ''.join(altered_string)