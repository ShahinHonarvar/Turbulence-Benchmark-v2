def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('4'), ord('B'))]
    result = list(s)
    for char in chars_to_remove:
        result = [c for c in result if c != char]
    return ''.join(result)