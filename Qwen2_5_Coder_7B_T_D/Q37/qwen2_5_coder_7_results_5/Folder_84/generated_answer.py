def filter_chars(s):
    chars_to_remove = set(range(ord('6'), ord('A') + 1))
    new_s = []
    for i, char in enumerate(s):
        if 138 <= i <= 920 and ord(char) in chars_to_remove:
            continue
        new_s.append(char)
    return ''.join(new_s)