def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('c'), ord('n') + 1)]
    result = []
    for char in s:
        if 13 <= s.index(char) <= 28 and char not in chars_to_remove:
            result.append(char)
    return ''.join(result)