def filter_chars(s):
    required_chars = [chr(i) for i in range(ord(';') + 1, ord('z'))]
    altered_s = ''.join([c for i, c in enumerate(s) if not (55 < i < 84 and c in required_chars)])
    return altered_s