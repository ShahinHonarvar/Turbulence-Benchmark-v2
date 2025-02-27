def filter_chars(my_string):
    substring = my_string[22:86]
    filtered_string = ''
    for char in substring:
        if char < '7' or char > 'e':
            filtered_string += char
    return filtered_string