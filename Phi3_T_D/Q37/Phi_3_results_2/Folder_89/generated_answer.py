def filter_chars(s):
    filtered_chars = set((chr(i) for i in range(ord('!'), ord('@') + 1)))
    new_string = ''.join((char for idx, char in enumerate(s) if idx < 11 or idx > 32 or char not in filtered_chars))
    return new_string