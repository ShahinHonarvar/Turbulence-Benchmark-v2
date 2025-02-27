def filter_chars(s):
    start, end = (227, 235)
    chars = [chr(i) for i in range(ord('D'), ord('u') + 1)]
    return ''.join((c for c in s if c not in chars[start - 227:end - 227 + 1]))