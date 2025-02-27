def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord(':'), ord('r') + 1)}
    result = ''.join([char for char in s if not (38 <= s.index(char) <= 54 and char in chars_to_remove)])
    return result