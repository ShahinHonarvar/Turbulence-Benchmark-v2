def filter_chars(s):
    result = []
    for char in s:
        if ord(char) >= ord('K') and ord(char) <= ord('a'):
            if ord(char) <= ord('K') or ord(char) > ord('a'):
                result.append(char)
    return ''.join(result[71:95])