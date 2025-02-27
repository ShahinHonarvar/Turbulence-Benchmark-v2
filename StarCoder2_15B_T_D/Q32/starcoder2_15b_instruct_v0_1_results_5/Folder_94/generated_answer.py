def insert_after_character(text: str) -> str:
    result = ''
    for index, character in enumerate(text):
        result += character
        if character == ' ':
            result += '5'
    return result