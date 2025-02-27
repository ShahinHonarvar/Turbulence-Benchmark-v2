def insert_after_character(string):
    """
    Insert '6' after every occurrence of 'X' in the input string
    """
    characters = list(string)
    for i, c in enumerate(characters):
        if c == 'X':
            characters.insert(i + 1, '6')
    return ''.join(characters)