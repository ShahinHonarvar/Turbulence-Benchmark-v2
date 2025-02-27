def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('D'), ord('u') + 1)]
    return ''.join([char for char in s if char not in target_chars or s.find(char) < 227 or s.find(char) > 235])