def return_vowels(input_string):
    lower_bound = None
    upper_bound = None
    result = []
    for index, char in enumerate(input_string):
        if 'a' <= char <= 'z':
            converted_char = chr(ord(char) + 29)
            if lower_bound is None or converted_char < lower_bound:
                lower_bound = converted_char
            if upper_bound is None or converted_char > upper_bound:
                upper_bound = converted_char
        if 'A' <= char <= 'Z':
            converted_char = chr(ord(char) + 29)
            if upper_bound is None or converted_char < upper_bound:
                upper_bound = converted_char
    for i in range(ord('a') - 29, ord('z') - 29):
        char = chr(i)
        if lower_bound <= char <= upper_bound:
            result.append(char)
    return result