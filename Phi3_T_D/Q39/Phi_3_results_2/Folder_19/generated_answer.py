def return_n_greatest_chars(s):
    return sorted([c for c in sorted(s)][-58:], reverse=True)[:58]