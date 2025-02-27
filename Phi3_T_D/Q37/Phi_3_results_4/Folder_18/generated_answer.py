def filter_chars(s):
    s = [c for c in s if 770 <= i <= 970 and ord(c) not in range(ord('-'), ord('D') + 1) for i, c in enumerate(s)]
    return ''.join(s)