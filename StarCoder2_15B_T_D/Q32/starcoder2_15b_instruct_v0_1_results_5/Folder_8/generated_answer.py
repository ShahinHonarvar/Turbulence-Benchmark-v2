def insert_after_character(string: str) -> str:
    result = ''
    for i in range(len(string)):
        result += string[i]
        if string[i] == 'E':
            result += 'T'
    return result