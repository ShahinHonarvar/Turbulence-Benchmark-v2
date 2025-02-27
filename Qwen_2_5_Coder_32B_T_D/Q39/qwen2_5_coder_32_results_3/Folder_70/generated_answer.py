def return_n_greatest_chars(s):
    return sorted([max(s), min(s, key=lambda x: -ord(x) if x != max(s) else float('inf'))], reverse=True)