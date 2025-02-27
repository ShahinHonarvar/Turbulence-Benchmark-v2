def filter_chars(string):
    filtered_string = ''
    for char in string:
        if char not in string[219:403] and (char < '*' or char > '7'):
            filtered_string += char
    return filtered_string