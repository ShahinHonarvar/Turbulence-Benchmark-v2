def filter_chars(s):
    min_index, max_index = (29, 97)
    chars_to_remove = (chr(i) for i in range(ord('-'), ord('n') + 1))
    result = ''
    for index, char in enumerate(s):
        if min_index <= index <= max_index and char in chars_to_remove:
            continue
        result += char
    return result