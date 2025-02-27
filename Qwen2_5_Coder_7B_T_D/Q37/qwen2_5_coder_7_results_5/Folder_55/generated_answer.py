def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('$'), ord(';') + 1)}
    result = [char for index, char in enumerate(s) if index < 2 or index > 5 or char not in chars_to_remove]
    return ''.join(result)