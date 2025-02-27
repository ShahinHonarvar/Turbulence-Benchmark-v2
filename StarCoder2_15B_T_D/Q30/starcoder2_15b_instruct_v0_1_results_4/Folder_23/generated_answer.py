def insert_before_character(text: str, char_to_insert: str, target_char: str) -> str:
    result = ''
    for char in text:
        if char == target_char:
            result += char_to_insert
        result += char
    return result