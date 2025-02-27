def filter_chars(s):
    chars_to_remove = set(range(ord('!'), ord('@') + 1))
    new_s = ''.join((char for char in s if 11 <= s.index(char) <= 32 and ord(char) not in chars_to_remove))
    return new_s