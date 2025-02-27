def filter_chars(input_string):
    return ''.join((c for c in input_string if not (477 <= ord(c) <= 984 and ',' <= c <= 'V')))