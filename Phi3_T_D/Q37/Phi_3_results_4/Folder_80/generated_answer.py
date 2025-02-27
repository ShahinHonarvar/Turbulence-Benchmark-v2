def filter_chars(s):
    filtered_chars = [char for char in s if not ('a' <= char <= 'i' and 36 <= s.find(char) <= 79)]
    return ''.join(filtered_chars)