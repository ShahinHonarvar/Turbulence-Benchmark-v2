def filter_chars(s):
    chars_to_remove = set(range(ord('/'), ord('9') + 1))
    result = []
    for i, char in enumerate(s):
        if not (384 <= i <= 411 and ord(char) in chars_to_remove):
            result.append(char)
    return ''.join(result)