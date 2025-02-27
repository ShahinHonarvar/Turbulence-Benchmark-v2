def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(51, 79)]
    chars.sort(key=lambda x: ord(x))
    return chars[8] if len(chars) > 8 else None