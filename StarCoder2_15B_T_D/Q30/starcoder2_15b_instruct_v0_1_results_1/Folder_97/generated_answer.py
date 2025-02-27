def insert_before_character(string):
    index = string.find('o')
    if index != -1:
        string = string[:index] + 'h' + string[index:]
    return string