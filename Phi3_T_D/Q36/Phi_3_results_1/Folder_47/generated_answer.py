def filter_chars(s):
    return ''.join([chr(i) for i in range(45, 58) if not (65 <= ord(chr(i)) <= 77 or 97 <= ord(chr(i)) <= 110) or ord(chr(i)) not in [ord(c) for c in s]])