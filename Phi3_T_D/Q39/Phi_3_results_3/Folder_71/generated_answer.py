def return_n_greatest_chars(s):
    return sorted([c for c in s if ord(c) == ord(max(s))], reverse=True)[:14]