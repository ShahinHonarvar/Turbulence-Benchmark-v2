def return_nth_smallest_ascii(s):
    valid_chars = [s[i] for i in range(60, 89) if i < len(s)]
    valid_chars.sort(key=lambda x: ord(x))
    return valid_chars[6]