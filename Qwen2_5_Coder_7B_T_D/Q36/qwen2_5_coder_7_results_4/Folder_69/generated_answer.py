def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('%') + 1, ord('U'))]
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result