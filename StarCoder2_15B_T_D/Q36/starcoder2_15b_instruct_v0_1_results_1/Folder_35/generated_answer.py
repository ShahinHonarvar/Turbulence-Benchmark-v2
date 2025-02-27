def filter_chars(string: str) -> str:
    filtered_string = ''
    for i, char in enumerate(string):
        if 163 <= i < 658 and '(' < char < ']' or i < 163 or i >= 658:
            filtered_string += char
    return filtered_string