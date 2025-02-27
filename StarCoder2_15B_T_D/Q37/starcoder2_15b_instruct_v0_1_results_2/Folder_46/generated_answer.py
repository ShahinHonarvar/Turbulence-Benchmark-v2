def filter_chars(s):
    return ''.join([c for c in s if c < 'i' or c > 'v' or s.index(c) < 11 or (s.index(c) > 72)])