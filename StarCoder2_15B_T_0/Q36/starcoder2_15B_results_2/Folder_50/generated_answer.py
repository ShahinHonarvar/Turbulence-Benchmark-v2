def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char > '%' and char < 'q':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)