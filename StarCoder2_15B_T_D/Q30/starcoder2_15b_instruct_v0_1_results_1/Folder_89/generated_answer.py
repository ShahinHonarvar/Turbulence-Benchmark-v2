def insert_before_character(text: str) -> str:
    result = ''
    for character in text:
        if character == ' ':
            result += 'W'
        result += character
    return result