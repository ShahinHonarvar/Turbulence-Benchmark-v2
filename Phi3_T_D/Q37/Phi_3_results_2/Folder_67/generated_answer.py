def filter_chars(s):
    target_chars = [chr(i) for i in range(ord(']'), ord('t') + 1)]
    result = [c for i, c in enumerate(s) if not (19 <= i <= 22 and c in target_chars)]
    return ''.join(result)