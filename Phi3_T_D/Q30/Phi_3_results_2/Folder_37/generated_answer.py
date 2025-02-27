def insert_before_character(input_str):
    result = ''
    for char in input_str:
        if char.lower() == 'u':
            result += 'a'
        result += char
    return result