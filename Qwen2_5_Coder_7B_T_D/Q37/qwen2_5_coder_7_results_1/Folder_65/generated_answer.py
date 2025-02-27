def filter_chars(s):
    indices_to_remove = {chr(i) for i in range(ord('0'), ord('@') + 1) if 61 <= i <= 70}
    return ''.join((c for c in s if c not in indices_to_remove))