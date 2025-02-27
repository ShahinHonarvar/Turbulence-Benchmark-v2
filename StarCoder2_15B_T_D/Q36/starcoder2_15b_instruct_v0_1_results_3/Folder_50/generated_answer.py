def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char > '%' and char < 'q' or (char < '%' or char > 'q'):
            filtered_chars.append(char)
    filtered_string = ''.join(filtered_chars)
    return filtered_string