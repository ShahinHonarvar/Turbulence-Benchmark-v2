def filter_chars(s, k):
    to_remove = set()
    for char in s:
        if ' ' <= char <= k:
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))