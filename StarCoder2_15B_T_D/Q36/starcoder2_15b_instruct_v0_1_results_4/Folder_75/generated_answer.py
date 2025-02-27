def filter_chars(string):
    start_index = 46
    end_index = 74
    filtered_string = ''
    for i, char in enumerate(string):
        if start_index <= i < end_index and '&' < char < 'M':
            continue
        filtered_string += char
    return filtered_string