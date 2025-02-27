def return_nth_smallest_ascii(s):
    start, end = (44, 69)
    chars = [ord(c) for c in s[start:end + 1]]
    return chr(sorted(chars)[-14])