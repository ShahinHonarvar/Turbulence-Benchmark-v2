def filter_chars(string: str) -> str:
    chars_to_remove = []
    for i, char in enumerate(string):
        if 82 < i < 89 and '*' < char < '[':
            chars_to_remove.append(char)
    filtered_string = ''.join((char for char in string if char not in chars_to_remove))
    return filtered_string