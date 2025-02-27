def filter_chars(string):
    char_count = 0
    for char in string:
        if char >= '5' and char <= '<':
            char_count += 1
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 24 or i > 82 or char < '5' or (char > '<'):
            filtered_string += char
    return filtered_string