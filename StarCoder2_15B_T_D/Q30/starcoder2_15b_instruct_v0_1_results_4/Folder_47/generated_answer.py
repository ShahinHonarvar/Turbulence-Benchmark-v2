def insert_before_character(string):
    """
    Insert 'f' before every occurrence of 'E' in the given string.
    """
    result = ''
    for char in string:
        if char == 'E':
            result += 'fE'
        else:
            result += char
    return result