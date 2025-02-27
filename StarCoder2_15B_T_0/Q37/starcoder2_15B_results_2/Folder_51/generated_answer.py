def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'H' or char > 'e' or (char < 'H' and char > 'e'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)