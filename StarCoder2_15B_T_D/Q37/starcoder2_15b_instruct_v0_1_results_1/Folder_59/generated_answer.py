def filter_chars(string):
    filtered_chars = [c for i, c in enumerate(string) if not (2 <= i <= 3 and '5' <= c <= '_')]
    return ''.join(filtered_chars)