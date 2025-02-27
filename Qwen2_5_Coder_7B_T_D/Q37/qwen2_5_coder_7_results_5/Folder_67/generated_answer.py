def filter_chars(s):
    chars_to_remove = set('[]{};:,.<>?`~@#$%^&*()_+=-')
    result = []
    for i, char in enumerate(s):
        if 19 <= i <= 22 and char not in chars_to_remove:
            result.append(char)
    return ''.join(result)