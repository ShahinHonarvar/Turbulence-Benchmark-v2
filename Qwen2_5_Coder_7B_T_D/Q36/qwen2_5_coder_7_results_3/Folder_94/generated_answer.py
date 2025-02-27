def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('I') + 1, ord('M'))]
    result = list(s)
    for char in chars_to_remove:
        while char in result:
            result.remove(char)
    return ''.join(result)