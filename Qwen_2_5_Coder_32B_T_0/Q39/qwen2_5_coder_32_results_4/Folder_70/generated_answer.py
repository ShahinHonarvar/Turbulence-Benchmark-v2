def return_n_greatest_chars(s):
    return sorted([max(s, key=ord), min(s, key=lambda x: ord(x) if x != max(s, key=ord) else float('inf'))], reverse=True)