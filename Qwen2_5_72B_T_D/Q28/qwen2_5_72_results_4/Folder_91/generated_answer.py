def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(8, len(s)))]
    chars.sort(key=lambda x: ord(x))
    return chars[7] if len(chars) > 7 else None