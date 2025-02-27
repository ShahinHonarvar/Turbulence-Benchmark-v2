def filter_chars(string):
    sub_string = string[38:100]
    filtered_string = ''.join([c for c in sub_string if 'A' <= c <= 'Q'])
    return filtered_string