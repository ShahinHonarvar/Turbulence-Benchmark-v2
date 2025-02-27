def remove_repeat_chars(string):
    unique_chars = set()
    result = ''
    for char in string:
        if char not in unique_chars:
            unique_chars.add(char)
            result += char
    return result