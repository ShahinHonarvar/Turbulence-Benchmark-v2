def filter_chars(s):
    chars_to_remove = set()
    for i, c in enumerate(s):
        if 12 <= i <= 77 and ord(c) in range(ord(':'), ord('L') + 1):
            chars_to_remove.add(c)
    filtered_chars = [c for c in s if c not in chars_to_remove]
    return ''.join(filtered_chars)