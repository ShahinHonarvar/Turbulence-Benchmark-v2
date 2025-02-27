def filter_chars(s):
    to_remove = [chr(i) for i in range(ord('#') + 1, ord('L'))]
    result = [char for char in s if char not in to_remove]
    return ''.join(result)