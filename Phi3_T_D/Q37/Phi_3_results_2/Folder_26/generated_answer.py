def filter_chars(s, i, k):
    filtered = ''.join([char for index, char in enumerate(s) if index < 20 or index > 62 or char < i or (char > k)])
    return filtered