def filter_chars(string):
    part_to_filter = string[88:91]
    for char in part_to_filter:
        if 'J' <= char <= 'Q':
            string = string.replace(char, '')
    return string