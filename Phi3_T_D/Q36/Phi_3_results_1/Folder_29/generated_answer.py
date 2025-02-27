def filter_chars(text):
    begin = 46
    end = 68
    char_limit = 'h'
    for i in range(begin, end):
        if 'A' <= text[i] <= char_limit:
            text = text.replace(text[i], '')
    return text