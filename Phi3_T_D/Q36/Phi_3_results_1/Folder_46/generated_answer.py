def filter_chars(s):
    start, end = (19, 69)
    take_out = ''.join([chr(i) for i in range(ord('<'), ord('C'))])
    return ''.join([char for char in s if not start <= ord(char) < end or char in take_out])