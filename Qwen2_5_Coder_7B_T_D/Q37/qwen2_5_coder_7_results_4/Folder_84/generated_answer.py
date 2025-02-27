def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('6'), ord('A') + 1)}
    result = []
    for i, char in enumerate(s):
        if not 138 <= i <= 920 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)