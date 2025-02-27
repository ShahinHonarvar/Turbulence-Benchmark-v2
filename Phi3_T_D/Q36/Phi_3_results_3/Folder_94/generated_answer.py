def filter_chars(s):
    start_index, end_index = (15, 85)
    char_set = set((chr(x) for x in range(ord('I'), ord('M'))))
    new_string = [s[i] for i in range(len(s)) if not start_index <= i < end_index or s[i] not in char_set]
    return ''.join(new_string)