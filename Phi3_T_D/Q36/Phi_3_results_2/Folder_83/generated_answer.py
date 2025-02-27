def filter_chars(s):
    altered_chars = [c if c > 'H' and c < 'I' else '' for c in s]
    return ''.join(altered_chars)