def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s[47:81]]
    unique_ascii_chars = set(ascii_chars)
    fourth_smallest_ascii = sorted(unique_ascii_chars)[3]
    return chr(fourth_smallest_ascii)