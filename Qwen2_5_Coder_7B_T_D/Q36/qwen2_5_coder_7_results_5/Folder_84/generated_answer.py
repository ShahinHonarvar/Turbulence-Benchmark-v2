def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('c') + 1, ord('s'))]
    result = []
    for char in s:
        if s.index(char) not in range(171, 636) or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)