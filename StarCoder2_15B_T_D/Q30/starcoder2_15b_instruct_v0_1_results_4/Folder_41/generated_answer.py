def insert_before_character(string: str) -> str:
    index = string.find('O')
    if index != -1:
        string = string.replace('O', 'oO')
    return string