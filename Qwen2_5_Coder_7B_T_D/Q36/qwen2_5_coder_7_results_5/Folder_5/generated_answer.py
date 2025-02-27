def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('g'), ord('|'))]
    result = []
    for char in s:
        if not (55 < ord(char) < 66 and char in chars_to_remove):
            result.append(char)
    return ''.join(result)