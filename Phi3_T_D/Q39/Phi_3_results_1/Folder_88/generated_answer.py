def return_n_greatest_chars(s: str):
    return sorted((c for c in s), key=ord, reverse=True)[:84]