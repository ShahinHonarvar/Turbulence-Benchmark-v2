def filter_chars(string):
    substring = string[323:526]
    for char in substring:
        if char > ')' and char < 'O':
            string = string.replace(char, '')
    return string