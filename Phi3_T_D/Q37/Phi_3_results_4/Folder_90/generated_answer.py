def filter_chars(s):
    indices = range(348, 853)
    filtered = [ch for i, ch in enumerate(s) if ch not in 'Jkmnl' or i not in indices]
    return ''.join(filtered)