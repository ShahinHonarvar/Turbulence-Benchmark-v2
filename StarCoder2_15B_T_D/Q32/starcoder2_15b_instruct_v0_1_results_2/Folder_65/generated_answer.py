def insert_after_character(string):
    result = ''
    for i in range(len(string) - 1):
        if string[i] == '6':
            result += '69'
        else:
            result += string[i]
    result += string[-1]
    return result