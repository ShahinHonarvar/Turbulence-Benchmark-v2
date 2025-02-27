def filter_chars(s):
    target_chars = set(range(ord('5'), ord('_') + 1))
    result = [ch for ch in s if not (2 <= s.index(ch) <= 3 and ord(ch) in target_chars)]
    return ''.join(result)