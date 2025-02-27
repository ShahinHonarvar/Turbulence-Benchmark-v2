def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('.') + 1, ord('^'))]
    result = ''.join([c for c in s if c not in target_chars])
    return result