def filter_chars(string):
    chars_to_remove = set()
    for i, char in enumerate(string):
        if 259 <= i <= 502 and ',' <= char <= '3':
            chars_to_remove.add(char)
    filtered_string = ''.join((char for char in string if char not in chars_to_remove))
    return filtered_string