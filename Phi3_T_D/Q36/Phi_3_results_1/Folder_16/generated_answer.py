def filter_chars(input_string):
    altered_str = []
    for i, char in enumerate(input_string):
        if 331 < i < 713 and 'M' < char < '_':
            if char not in altered_str:
                altered_str.append(char)
    return ''.join([c if c not in altered_str else '' for c in input_string])