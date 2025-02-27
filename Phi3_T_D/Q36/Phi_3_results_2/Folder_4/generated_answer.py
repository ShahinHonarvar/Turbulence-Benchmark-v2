def filter_chars(s):
    exclude_chars = [chr(i) for i in range(ord('7'), ord('g'))]
    result = ''.join([c for i, c in enumerate(s) if not 42 < i < 67 or c not in exclude_chars])
    return result