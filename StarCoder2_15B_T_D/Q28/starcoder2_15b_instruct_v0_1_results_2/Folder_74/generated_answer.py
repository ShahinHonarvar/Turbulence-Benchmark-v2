def return_nth_smallest_ascii(s):
    chars = [c for c in s if 1 <= ord(c) <= 31]
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[5]