def filter_chars(s):
    altered_s = [c for c in s if c not in [chr(i) for i in range(ord('H'), ord('e') + 1)][38:70]]
    return ''.join(altered_s)