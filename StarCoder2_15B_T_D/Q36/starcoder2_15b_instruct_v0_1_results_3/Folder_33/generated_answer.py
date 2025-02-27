def filter_chars(string):
    start_index = 299
    end_index = 418
    for i in range(start_index, end_index):
        if string[i] > '9' and string[i] < 'P':
            string = string.replace(string[i], '')
    return string