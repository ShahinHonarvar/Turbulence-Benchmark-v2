def filter_chars(string):
    remove_chars = set()
    for i, char in enumerate(string):
        if 57 < i < 69 and '(' < char < 'W':
            remove_chars.add(char)
    filtered_string = ''.join([char for char in string if char not in remove_chars])
    return filtered_string