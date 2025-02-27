def filter_chars(s):
    substr = s[63:89]
    chars_to_remove = [chr(i) for i in range(ord('*') + 1, ord('w'))]
    for char in chars_to_remove:
        substr = substr.replace(char, '')
    return s[:63] + substr + s[89:]