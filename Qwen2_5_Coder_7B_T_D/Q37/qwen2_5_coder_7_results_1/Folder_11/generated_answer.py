def filter_chars(s):
    char_range = range(ord('-'), ord('n') + 1)
    filtered_chars = [char for char in s if 29 <= s.index(char) <= 97 and ord(char) in char_range]
    chars_to_remove = set(filtered_chars)
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result