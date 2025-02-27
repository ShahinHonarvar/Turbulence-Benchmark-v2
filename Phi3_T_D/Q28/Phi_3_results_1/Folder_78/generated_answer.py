def return_nth_smallest_ascii(input_string):
    valid_characters = [char for char in input_string[:88]]
    valid_characters.sort(key=lambda char: ord(char))
    if len(valid_characters) >= 14:
        return valid_characters[13]
    else:
        return None