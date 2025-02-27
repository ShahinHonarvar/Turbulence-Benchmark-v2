def return_nth_smallest_ascii(s):
    indexed_chars = [(ord(c), i) for i, c in enumerate(s, 1) if 17 <= i <= 34]
    indexed_chars.sort(key=lambda x: x[0])
    return chr(indexed_chars[7][0]) if len(indexed_chars) >= 18 else None