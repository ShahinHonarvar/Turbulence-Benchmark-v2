def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i < 61 or i >= 88 or (char <= '%' or char >= 'q'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)