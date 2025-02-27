def filter_chars(s):
    exclude_chars = ''.join((chr(i) for i in range(ord('H'), ord('|') if i >= ord('H') else ord('i') + 1)))
    filtered_str = ''.join((char for char in s if char not in exclude_chars or not 18 < s.index(char) < 31))
    return filtered_str