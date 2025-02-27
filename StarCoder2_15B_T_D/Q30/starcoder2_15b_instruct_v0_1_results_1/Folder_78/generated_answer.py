def insert_before_character(text: str) -> str:
    """
    Inserts the character's' immediately preceding any occurrences of the character 'H' in the input string.
    """
    output = []
    for character in text:
        if character == 'H':
            output.append('s')
        output.append(character)
    return ''.join(output)