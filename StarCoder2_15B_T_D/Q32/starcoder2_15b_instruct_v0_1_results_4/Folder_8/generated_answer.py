def insert_after_character(string: str) -> str:
    characters = list(string)
    for i, character in enumerate(characters):
        if character == 'E':
            characters.insert(i + 1, 'T')
    return ''.join(characters)