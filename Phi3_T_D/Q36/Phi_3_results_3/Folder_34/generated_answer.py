def filter_chars(s):
    start, end = (10, 79)
    valid_range = set('@ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = []
    for i, char in enumerate(s):
        if start < i < end and char in valid_range:
            result.append((i, char))
    altered_s = list(s)
    indices_to_remove = [idx for i, char in sorted(result, key=lambda x: x[0]) for idx in range(i, len(s)) if altered_s[idx] == char]
    for idx in reversed(indices_to_remove):
        del altered_s[idx]
    return ''.join(altered_s)