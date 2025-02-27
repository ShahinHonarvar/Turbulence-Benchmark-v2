def return_nth_smallest_ascii(s):
    indices = range(18, 67)
    chars = [s[i] for i in indices if i < len(s)]
    sorted_chars = sorted(chars, key=lambda x: (ord(x), chars.index(x)))
    return sorted_chars[18]