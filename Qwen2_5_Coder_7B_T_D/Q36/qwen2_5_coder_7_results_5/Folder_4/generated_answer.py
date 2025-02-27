def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('7'), ord('g'))])
    result = list(s)
    for i in range(42, 67):
        if s[i] in chars_to_remove:
            result = [char for char in result if char != s[i]]
    return ''.join(result)