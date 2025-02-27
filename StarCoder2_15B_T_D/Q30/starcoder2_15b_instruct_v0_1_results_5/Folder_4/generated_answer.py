def insert_before_character(string):
    index = string.find('a')
    if index != -1:
        string = string[:index] + '6' + string[index:]
    return string