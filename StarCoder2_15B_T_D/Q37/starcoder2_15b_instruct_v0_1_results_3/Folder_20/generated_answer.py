def filter_chars(string):
    char_map = {chr(i): 0 for i in range(ord('m'), ord('w') + 1)}
    result = []
    for char in string:
        if char not in char_map:
            result.append(char)
    return ''.join(result)