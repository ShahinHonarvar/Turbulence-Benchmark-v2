def filter_chars(s):
    start, end = (421, 854)
    range_characters = set((chr(ord('E') + i) for i in range(ord('F'), ord('I'))))
    filtered_list = [char for char in s if char not in s[start:end] or char not in range_characters]
    return ''.join(filtered_list)