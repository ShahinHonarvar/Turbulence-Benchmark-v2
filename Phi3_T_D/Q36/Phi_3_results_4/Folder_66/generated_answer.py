def filter_chars(s):
    exclude_chars = [chr(i) for i in range(ord('!') + 1, ord('}') - (87 - 39))]
    result = ''.join([char for char in s if char not in exclude_chars or (s.index(char) >= 39 and s.index(char) < 87)])
    return result