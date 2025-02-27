def filter_chars(string):
    start_index = 323
    end_index = 526
    invalid_chars = ')'
    valid_chars = 'O'
    filtered_string = ''
    for char in string:
        if char > invalid_chars and char < valid_chars:
            continue
        filtered_string += char
    return filtered_string